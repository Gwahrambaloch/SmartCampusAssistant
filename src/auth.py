import hashlib
import sqlite3
from src.database import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, email):
    conn = get_connection()
    cursor = conn.cursor()
    
    hashed_pw = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
                       (username, hashed_pw, email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    
    hashed_pw = hash_password(password)
    
    cursor.execute("SELECT id, username FROM users WHERE username = ? AND password = ?", 
                   (username, hashed_pw))
    user = cursor.fetchone()
    conn.close()
    
    return user

def get_user_stats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
