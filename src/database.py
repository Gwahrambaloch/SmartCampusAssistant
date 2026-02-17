import sqlite3
import os

DB_FILE = "campus_assistant.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT
        )
    """)

    # Tasks Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            description TEXT,
            deadline DATE,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    # Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT NOT NULL,
            date DATE,
            status TEXT CHECK(status IN ('Present', 'Absent')),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    # Grades Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT NOT NULL,
            marks REAL,
            total_marks REAL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
