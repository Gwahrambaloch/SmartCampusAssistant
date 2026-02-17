import sqlite3
from src.database import get_connection
import pandas as pd

def add_grade(user_id, subject, marks, total_marks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (user_id, subject, marks, total_marks) VALUES (?, ?, ?, ?)",
                   (user_id, subject, marks, total_marks))
    conn.commit()
    conn.close()

def get_grades(user_id):
    conn = get_connection()
    query = "SELECT subject, marks, total_marks FROM grades WHERE user_id = ?"
    df = pd.read_sql_query(query, conn, params=(user_id,))
    conn.close()
    
    if not df.empty:
        df['Percentage'] = (df['marks'] / df['total_marks']) * 100
        
    return df

def calculate_gpa(user_id):
    df = get_grades(user_id)
    if df.empty:
        return 0.0
    
    # Simple average percentage as a proxy for GPA for now, or actual GPA logic if needed.
    # Let's assume a simple 4.0 scale based on percentage.
    # >90: 4.0, >80: 3.5, etc.
    
    def grade_point(percentage):
        if percentage >= 90: return 4.0
        elif percentage >= 80: return 3.5
        elif percentage >= 70: return 3.0
        elif percentage >= 60: return 2.5
        elif percentage >= 50: return 2.0
        else: return 0.0

    avg_percentage = df['Percentage'].mean()
    return grade_point(avg_percentage) # Return average GPA
