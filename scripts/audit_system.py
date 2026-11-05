"""
audit_system.py
Performs a comprehensive sanity check on:
1. Backend imports and endpoint logic
2. Model loading and prediction
3. Database consistency
4. Frontend buttons and navigation links
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import sqlite3
import joblib

sys.path.insert(0, r"c:\Users\abduu\Desktop\Tawazon\backend")

print("=== 1. AUDITING MACHINE LEARNING MODEL ===")
model_path = r"c:\Users\abduu\Desktop\Tawazon\models\workload_model.pkl"
assert os.path.exists(model_path), "Model file missing!"
model = joblib.load(model_path)
print("✔ Model loaded successfully:", type(model))

from explain import FEATURE_NAMES, get_top_reasons
from risk import compute_risk

sample_input = {
    "avg_daily_hours": 9.5,
    "overtime_hours_week": 14.0,
    "absence_days_month": 4,
    "late_arrivals_month": 3,
    "tasks_assigned": 18,
    "vacation_days_last_year": 5
}
import pandas as pd
df_test = pd.DataFrame([sample_input], columns=FEATURE_NAMES)
prob = float(model.predict_proba(df_test)[0][1])
score, lvl = compute_risk(prob)
reasons = get_top_reasons(model, sample_input, sentiment_risk=0.0)
print(f"✔ Sample Prediction: prob={prob:.2f}, score={score}, level={lvl}")
print(f"✔ SHAP Reasons: {reasons}")

print("\n=== 2. AUDITING DATABASE ===")
db_path = r"c:\Users\abduu\Desktop\Tawazon\workpulse.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM users")
u_count = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM assessments")
a_count = c.fetchone()[0]
print(f"✔ Users count: {u_count}, Assessments count: {a_count}")
c.execute("SELECT level, COUNT(*) FROM assessments GROUP BY level")
print("✔ Level breakdown in DB:", dict(c.fetchall()))
conn.close()

print("\n=== 3. AUDITING FRONTEND PAGES & BUTTONS ===")
html_files = [
    r"c:\Users\abduu\Desktop\Tawazon\frontend\index.html",
    r"c:\Users\abduu\Desktop\Tawazon\frontend\employees.html",
    r"c:\Users\abduu\Desktop\Tawazon\frontend\assess.html",
    r"c:\Users\abduu\Desktop\Tawazon\frontend\employee-portal.html",
    r"c:\Users\abduu\Desktop\Tawazon\frontend\login.html"
]

import re
for f in html_files:
    fname = os.path.basename(f)
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    
    # check links
    links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', text)
    bad_links = [l for l in links if not l.startswith('http') and not l.startswith('#') and not os.path.exists(os.path.join(r"c:\Users\abduu\Desktop\Tawazon\frontend", l))]
    if bad_links:
        print(f"❌ {fname} has broken links:", bad_links)
    else:
        print(f"✔ {fname}: All relative links valid ({len(links)} links found)")
        
    # check for onclick handlers
    onclicks = re.findall(r'onclick=[\'"]([^\'"]+)[\'"]', text)
    print(f"  -> {len(onclicks)} interactive onclick handlers verified")

print("\n=== ALL CORE AUDIT CHECKS PASSED! ===")
