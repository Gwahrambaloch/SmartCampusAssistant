import streamlit as st
import pandas as pd
from src import auth, reminders, database

# Set page config at the very top
st.set_page_config(page_title="Smart Campus Assistant", page_icon="🎓", layout="wide")

def login_page():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = auth.login_user(username, password)
        if user:
            st.success(f"Welcome back, {user[1]}!")
            st.session_state['user_id'] = user[0]
            st.session_state['username'] = user[1]
            st.rerun()
        else:
            st.error("Invalid username or password")

def register_page():
    st.title("📝 Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match")
        else:
            if auth.register_user(username, password, email):
                st.success("Registration successful! Please login.")
            else:
                st.error("Username already exists")

def dashboard():
    st.title(f"🎓 Welcome, {st.session_state['username']}!")
    
    st.markdown("### 📢 Notifications")
    upcoming = reminders.get_upcoming_deadlines(st.session_state['user_id'])
    
    if upcoming:
        for item in upcoming:
            st.warning(f"⚠️ **{item['task']}** is due in {item['days_left']} days ({item['deadline']})")
    else:
        st.info("🎉 No upcoming deadlines in the next 3 days.")

    st.markdown("---")
    st.markdown("### 🚀 Quick Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Pending Tasks", len(upcoming) if upcoming else "0") # Placeholder
    # We could fetch real stats here
    
    st.markdown("Navigate using the sidebar to manage Tasks, Attendance, and Grades.")
    
    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()



def main():
    # Ensure database tables exist
    database.create_tables()

    if 'user_id' not in st.session_state:
        menu = ["Login", "Register"]
        choice = st.sidebar.selectbox("Menu", menu)
        
        if choice == "Login":
            login_page()
        else:
            register_page()
    else:
        dashboard()

if __name__ == "__main__":
    main()
