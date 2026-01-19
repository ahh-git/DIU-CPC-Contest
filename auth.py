import streamlit as st

def google_login():
    user = st.experimental_user
    if not user.email.endswith("@diu.edu.bd"):
        st.error("Only diu.edu.bd email allowed")
        st.stop()
    return user.name, user.email