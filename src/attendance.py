import sqlite3
from src.database import get_connection
import pandas as pd

def mark_attendance(user_id, subject, date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (user_id, subject, date, status) VALUES (?, ?, ?, ?)",
                   (user_id, subject, date, status))
    conn.commit()
    conn.close()

def get_attendance_summary(user_id):
    conn = get_connection()
    query = "SELECT subject, status FROM attendance WHERE user_id = ?"
    df = pd.read_sql_query(query, conn, params=(user_id,))
    conn.close()
    
    if df.empty:
        return pd.DataFrame(columns=["Subject", "Total", "Present", "Percentage"])

    summary = df.groupby('subject')['status'].value_counts().unstack().fillna(0)
    
    # Ensure 'Present' and 'Absent' columns exist
    if 'Present' not in summary.columns:
        summary['Present'] = 0
    if 'Absent' not in summary.columns:
        summary['Absent'] = 0
        
    summary['Total'] = summary['Present'] + summary['Absent']
    summary['Percentage'] = (summary['Present'] / summary['Total']) * 100
    
    return summary.reset_index().rename(columns={"subject": "Subject"})
