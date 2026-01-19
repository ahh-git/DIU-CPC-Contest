import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    name TEXT,
    student_id TEXT,
    paid INTEGER,
    bio TEXT,
    pfp TEXT
)
""")
conn.commit()