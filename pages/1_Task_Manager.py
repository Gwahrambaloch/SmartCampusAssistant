import streamlit as st
import pandas as pd
from datetime import date
from src import tasks

st.set_page_config(page_title="Task Manager", page_icon="📝", layout="wide")

if 'user_id' not in st.session_state:
    st.warning("Please login first!")
    st.stop()

st.title("📝 Task & Assignment Manager")

with st.expander("➕ Add New Assignment"):
    title = st.text_input("Task Title")
    description = st.text_area("Description")
    deadline = st.date_input("Deadline", min_value=date.today())
    
    if st.button("Add Task"):
        if title:
            tasks.add_task(st.session_state['user_id'], title, description, str(deadline))
            st.success("Task added successfully!")
            st.rerun()
        else:
            st.error("Title is required")

st.markdown("### 📋 Your Assignments")
user_tasks = tasks.get_tasks(st.session_state['user_id'])

if user_tasks:
    df = pd.DataFrame(user_tasks, columns=['ID', 'Title', 'Description', 'Deadline', 'Status'])
    
    # Allow status update
    for index, row in df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 2, 1])
        with col1:
            st.write(f"**{row['Title']}**")
        with col2:
            st.write(row['Description'])
        with col3:
            st.write(f"📅 {row['Deadline']}")
        with col4:
            new_status = st.selectbox("Status", ["Pending", "Completed"], index=0 if row['Status'] == "Pending" else 1, key=f"status_{row['ID']}")
            if new_status != row['Status']:
                tasks.update_task_status(row['ID'], new_status)
                st.rerun()
        with col5:
            if st.button("🗑️", key=f"del_{row['ID']}"):
                tasks.delete_task(row['ID'])
                st.rerun()
else:
    st.info("No tasks found. Add a new one!")
