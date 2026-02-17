import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
from src import attendance

st.set_page_config(page_title="Attendance Tracker", page_icon="📅", layout="wide")

if 'user_id' not in st.session_state:
    st.warning("Please login first!")
    st.stop()

st.title("📅 Attendance Tracker")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Mark Attendance")
    subject = st.text_input("Subject Name")
    status = st.radio("Status", ["Present", "Absent"])
    attendance_date = st.date_input("Date", value=date.today())
    
    if st.button("Mark Attendance"):
        if subject:
            attendance.mark_attendance(st.session_state['user_id'], subject, str(attendance_date), status)
            st.success("Attendance marked!")
            st.rerun()
        else:
            st.error("Subject is required")

with col2:
    st.markdown("### 📊 Attendance Summary")
    summary = attendance.get_attendance_summary(st.session_state['user_id'])
    
    if not summary.empty:
        st.dataframe(summary)
        
        # Chart
        fig = px.bar(summary, x='Subject', y='Percentage', title="Attendance Percentage by Subject", range_y=[0, 100])
        st.plotly_chart(fig)
    else:
        st.info("No attendance records found.")
