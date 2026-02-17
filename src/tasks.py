import sqlite3
from src.database import get_connection

def add_task(user_id, title, description, deadline):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_id, title, description, deadline) VALUES (?, ?, ?, ?)",
                   (user_id, title, description, deadline))
    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, deadline, status FROM tasks WHERE user_id = ?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
