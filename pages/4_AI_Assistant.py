import streamlit as st

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="wide")

if 'user_id' not in st.session_state:
    st.warning("Please login first!")
    st.stop()

st.title("🤖 Campus AI Assistant")

st.markdown("Ask me anything about your campus life! (e.g., 'How to calculate GPA?', 'Tips for exams')")

user_query = st.text_input("Your Question:")

if user_query:
    query = user_query.lower()
    response = "I'm not sure about that, but keep studying hard! 📚"
    
    if "gpa" in query:
        response = "GPA is calculated by averaging your grade points. Check the Grade Calculator tab for your current GPA! 📈"
    elif "test" in query or "exam" in query:
        response = "Make sure to review your notes daily and get enough sleep before the exam! 😴"
    elif "attendance" in query:
        response = "75% attendance is usually required. Check the Attendance Tracker to see where you stand! 📅"
    elif "deadline" in query:
        response = "Check the Task Manager for upcoming deadlines! Don't procrastinate! ⏳"
        
    st.info(response)
