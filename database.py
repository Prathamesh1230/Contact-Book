import sqlite3

def connect():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()
