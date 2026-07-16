import sqlite3
from datetime import date

DB = "phetogo.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client TEXT NOT NULL,
            description TEXT NOT NULL,
            assigned_to TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            date_created TEXT DEFAULT CURRENT_DATE
        )
    ''')
    conn.commit()
    conn.close()

def get_tasks(search=None, status_filter=None):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []
    if search:
        query += " AND (client LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])
    if status_filter and status_filter != "All":
        query += " AND status = ?"
        params.append(status_filter)
    query += " ORDER BY id DESC"
    c.execute(query, params)
    tasks = c.fetchall()
    conn.close()
    return tasks

def add_task(client, description, assigned_to):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO tasks (client, description, assigned_to) VALUES (?, ?, ?)",
        (client, description, assigned_to)
    )
    conn.commit()
    conn.close()

def update_task_status(task_id, status):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def edit_task(task_id, client, description, assigned_to, status):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "UPDATE tasks SET client = ?, description = ?, assigned_to = ?, status = ? WHERE id = ?",
        (client, description, assigned_to, status, task_id)
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def get_task_by_id(task_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = c.fetchone()
    conn.close()
    return task

def get_report():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    today = date.today().isoformat()
    c.execute("SELECT COUNT(*) FROM tasks WHERE date_created = ?", (today,))
    total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM tasks WHERE status = 'Completed' AND date_created = ?", (today,))
    completed = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM tasks WHERE status = 'Pending' AND date_created = ?", (today,))
    pending = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM tasks WHERE status = 'In Progress' AND date_created = ?", (today,))
    in_progress = c.fetchone()[0]
    conn.close()
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "in_progress": in_progress,
        "date": today
    }