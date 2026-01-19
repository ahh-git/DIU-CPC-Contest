import streamlit as st
from database import c

def admin_panel():
    st.subheader("🔐 Admin Panel")
    pwd = st.text_input("Password", type="password")

    if pwd != "891011":
        st.error("Wrong password")
        return

    st.success("Admin access granted")
    data = c.execute("SELECT * FROM users").fetchall()
    st.dataframe(data)