import streamlit as st
import pandas as pd
from src import auth

st.set_page_config(page_title="User Stats", page_icon="👥", layout="wide")

if 'user_id' not in st.session_state:
    st.warning("Please login first!")
    st.stop()

# --- ADMIN ACCESS CONTROL ---
ADMIN_USER = "belbaloch"  # <--- CHANGE THIS to your actual username if it's not 'admin'

if st.session_state.get("username") != ADMIN_USER:
    st.error("⛔ Access Denied: This page is for administrators only.")
    st.stop()
# ----------------------------

st.title("👥 User Statistics")

users = auth.get_user_stats()
count = len(users)

st.metric(label="Total Registered Users", value=count)

st.markdown("### 📜 List of Users")

if users:
    df = pd.DataFrame(users, columns=["Username", "Email"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("No users found.")
