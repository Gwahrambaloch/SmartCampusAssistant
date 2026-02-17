import streamlit as st
import pandas as pd
from src import grades

st.set_page_config(page_title="Grade Calculator", page_icon="💯", layout="wide")

if 'user_id' not in st.session_state:
    st.warning("Please login first!")
    st.stop()

st.title("💯 Grade Calculator")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Add Grades")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks Obtained", min_value=0.0, step=0.5)
    total = st.number_input("Total Marks", min_value=1.0, value=100.0)
    
    if st.button("Add Grade"):
        if subject:
            grades.add_grade(st.session_state['user_id'], subject, marks, total)
            st.success("Grade added!")
            st.rerun()
        else:
            st.error("Subject is required")

with col2:
    st.markdown("### 🎓 Academic Performance")
    df = grades.get_grades(st.session_state['user_id'])
    
    if not df.empty:
        st.dataframe(df)
        gpa = grades.calculate_gpa(st.session_state['user_id'])
        st.metric(label="Estimated GPA (4.0 Scale)", value=f"{gpa:.2f}")
    else:
        st.info("No grades added yet.")
