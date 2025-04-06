import sqlite3

def add_contact(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contact (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_contact(name):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact WHERE name LIKE ?", ('%' + name + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contact WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

def update_contact(contact_id, name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("UPDATE contact SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()
