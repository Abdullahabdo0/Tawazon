import sqlite3
import joblib
import pandas as pd
import numpy as np

model = joblib.load(r'c:\Users\abduu\Desktop\Tawazon\models\workload_model.pkl')
print("Model loaded successfully:", type(model))

conn = sqlite3.connect(r'c:\Users\abduu\Desktop\Tawazon\workpulse.db')
c = conn.cursor()
c.execute("PRAGMA table_info(assessments)")
cols = [col[1] for col in c.fetchall()]
print("Columns in assessments:", cols)

# Read 5 rows
c.execute("SELECT id, avg_daily_hours, overtime_hours_week, absence_days_month, late_arrivals_month, tasks_assigned, vacation_days_last_year, risk_score, level FROM assessments LIMIT 5")
rows = c.fetchall()
for r in rows:
    feat = [[r[1], r[2], r[3], r[4], r[5], r[6]]]
    prob = model.predict_proba(feat)[0][1]
    new_score = int(round(prob * 100))
    new_lvl = "Low" if new_score < 34 else ("Medium" if new_score < 67 else "High")
    print(f"ID {r[0]}: old_score={r[7]} ({r[8]}) -> new_score={new_score} ({new_lvl})")
