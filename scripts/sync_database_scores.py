"""
sync_database_scores.py
Recalculates every employee assessment in workpulse.db using the retrained
Random Forest model (models/workload_model.pkl) without feedback or sentiment.
Sets sentiment_risk = 0.0, updates risk_score, level, workload_probability,
and top_reasons across the entire database.
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
from explain import get_top_reasons, FEATURE_NAMES

MODEL_PATH = r"c:\Users\abduu\Desktop\Tawazon\models\workload_model.pkl"
DB_PATHS = [
    r"c:\Users\abduu\Desktop\Tawazon\workpulse.db",
    r"c:\Users\abduu\Desktop\Tawazon\backend\workpulse.db"
]

print("Loading retrained Random Forest model...")
model = joblib.load(MODEL_PATH)
print("Model loaded successfully.")

for db_path in DB_PATHS:
    if not os.path.exists(db_path) or os.path.getsize(db_path) == 0:
        continue
    
    print(f"\nProcessing database: {db_path}...")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Check if assessments table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='assessments'")
    if not c.fetchone():
        print(f"No assessments table in {db_path}, skipping.")
        conn.close()
        continue
    
    c.execute("""
        SELECT id, avg_daily_hours, overtime_hours_week, absence_days_month,
               late_arrivals_month, tasks_assigned, vacation_days_last_year,
               risk_score, level
        FROM assessments
    """)
    rows = c.fetchall()
    print(f"Found {len(rows)} assessments to recalculate.")
    
    updated_count = 0
    levels_summary = {"Low": 0, "Medium": 0, "High": 0}
    
    for row in rows:
        a_id = row[0]
        feat_dict = {
            "avg_daily_hours": float(row[1] or 0),
            "overtime_hours_week": float(row[2] or 0),
            "absence_days_month": int(row[3] or 0),
            "late_arrivals_month": int(row[4] or 0),
            "tasks_assigned": int(row[5] or 0),
            "vacation_days_last_year": int(row[6] or 0),
        }
        
        # Predict with DataFrame so feature names are aligned
        df_input = pd.DataFrame([feat_dict], columns=FEATURE_NAMES)
        prob = float(model.predict_proba(df_input)[0][1])
        new_score, new_level = compute_risk(prob)
        levels_summary[new_level] += 1
        
        # Calculate clean top reasons based purely on workload SHAP
        reasons_list = get_top_reasons(model, feat_dict, sentiment_risk=0.0, top_n=3)
        reasons_json = json.dumps(reasons_list, ensure_ascii=False)
        
        c.execute("""
            UPDATE assessments
            SET risk_score = ?,
                level = ?,
                workload_probability = ?,
                sentiment_risk = 0.0,
                top_reasons = ?
            WHERE id = ?
        """, (new_score, new_level, round(prob, 4), reasons_json, a_id))
        
        updated_count += 1
        
    conn.commit()
    conn.close()
    print(f"Successfully updated {updated_count} records in {db_path}!")
    print(f"New Level Distribution: {levels_summary}")

print("\nDatabase rescore sync completed successfully!")
