from datetime import datetime, timedelta
import pandas as pd
from src.database import get_connection

def get_upcoming_deadlines(user_id, days=3):
    conn = get_connection()
    # SQLite date functions can be tricky, doing filtering in Python for simplicity
    cursor = conn.cursor()
    cursor.execute("SELECT title, deadline FROM tasks WHERE user_id = ? AND status != 'Completed'", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    
    upcoming = []
    today = datetime.now().date()
    threshold = today + timedelta(days=days)
    
    for title, deadline_str in tasks:
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            if today <= deadline <= threshold:
                days_left = (deadline - today).days
                upcoming.append({"task": title, "deadline": deadline_str, "days_left": days_left})
        except ValueError:
            pass # Ignore invalid dates
            
    return upcoming
