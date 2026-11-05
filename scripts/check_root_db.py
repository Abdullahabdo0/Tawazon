import sqlite3

conn = sqlite3.connect(r'c:\Users\abduu\Desktop\Tawazon\workpulse.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
print('Tables in root workpulse.db:', tables)

for t in tables:
    t_name = t[0]
    c.execute(f"SELECT COUNT(*) FROM {t_name}")
    cnt = c.fetchone()[0]
    print(f"Table {t_name}: {cnt} rows")

c.execute("SELECT level, count(*), ROUND(AVG(risk_score), 1) FROM assessments GROUP BY level")
print("Assessment levels & avg risk:", c.fetchall())

c.execute("SELECT AVG(sentiment_risk) FROM assessments")
print("Avg sentiment risk in DB:", c.fetchone()[0])

# Check a sample assessment
c.execute("SELECT id, user_id, risk_score, level, workload_prob, sentiment_risk FROM assessments LIMIT 5")
print("Sample assessments:", c.fetchall())
