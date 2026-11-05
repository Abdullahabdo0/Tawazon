"""
sync_database_scores_fast.py
Vectorized batch update of workpulse.db with the retrained Random Forest model.
Runs in under 1 second.
"""

import os
import sys
import json
import sqlite3
import joblib
import pandas as pd
import numpy as np

sys.path.insert(0, r"c:\Users\abduu\Desktop\Tawazon\backend")
from risk import compute_risk
from explain import FEATURE_NAMES, FEATURE_LABELS, _fallback_reasons

MODEL_PATH = r"c:\Users\abduu\Desktop\Tawazon\models\workload_model.pkl"
DB_PATH = r"c:\Users\abduu\Desktop\Tawazon\workpulse.db"

print("Loading model...")
model = joblib.load(MODEL_PATH)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""
    SELECT id, avg_daily_hours, overtime_hours_week, absence_days_month,
           late_arrivals_month, tasks_assigned, vacation_days_last_year
    FROM assessments
""")
rows = c.fetchall()
print(f"Loaded {len(rows)} rows from {DB_PATH}.")

df = pd.DataFrame([
    {
        "id": r[0],
        "avg_daily_hours": float(r[1] or 0),
        "overtime_hours_week": float(r[2] or 0),
        "absence_days_month": int(r[3] or 0),
        "late_arrivals_month": int(r[4] or 0),
        "tasks_assigned": int(r[5] or 0),
        "vacation_days_last_year": int(r[6] or 0),
    }
    for r in rows
])

X = df[FEATURE_NAMES]
probas = model.predict_proba(X)[:, 1]

update_data = []
levels_count = {"Low": 0, "Medium": 0, "High": 0}

for idx, row in df.iterrows():
    p = float(probas[idx])
    score, level = compute_risk(p)
    levels_count[level] += 1
    
    # Generate clean reasons using fast rule-based weights from tree
    feats = row.to_dict()
    reasons = _fallback_reasons(feats, top_n=3)
    reasons_json = json.dumps(reasons, ensure_ascii=False)
    
    update_data.append((score, level, round(p, 4), 0.0, reasons_json, int(row["id"])))

c.executemany("""
    UPDATE assessments
    SET risk_score = ?,
        level = ?,
        workload_probability = ?,
        sentiment_risk = ?,
        top_reasons = ?
    WHERE id = ?
""", update_data)

conn.commit()
conn.close()

print("FINISHED! Vectorized update complete.")
print(f"Summary of {len(update_data)} employees with retrained pure ML model:")
print(f"  Low risk   : {levels_count['Low']}")
print(f"  Medium risk: {levels_count['Medium']}")
print(f"  High risk  : {levels_count['High']}")
