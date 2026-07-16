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

def get_tasks():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY id DESC")
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
    c.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (status, task_id)
    )
    conn.commit()
    conn.close()

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