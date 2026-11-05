import sqlite3

conn = sqlite3.connect(r'c:\Users\abduu\Desktop\Tawazon\backend\workpulse.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
print('Tables in DB:', tables)

for t in tables:
    t_name = t[0]
    c.execute(f"SELECT COUNT(*) FROM {t_name}")
    cnt = c.fetchone()[0]
    print(f"Table {t_name}: {cnt} rows")

# If users table exists, check role and assessments
if ('users',) in tables:
    c.execute("SELECT id, username, full_name, role FROM users LIMIT 5")
    print("Sample users:", c.fetchall())

# Look for table with assessments or scores
for t in tables:
    if 'assess' in t[0] or 'risk' in t[0] or 'emp' in t[0]:
        c.execute(f"PRAGMA table_info({t[0]})")
        print(f"Columns in {t[0]}:", [col[1] for col in c.fetchall()])
