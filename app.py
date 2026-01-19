import streamlit as st
import re
from auth import google_login
from database import conn, c
from payment import bkash_payment
from admin import admin_panel

st.set_page_config("CPC Club Contest Spring 2026", layout="wide")

# hidden admin (double tap logo)
if "tap" not in st.session_state:
    st.session_state.tap = 0

st.image("assets/logo.png", width=120)
if st.button(" "):
    st.session_state.tap += 1
    if st.session_state.tap == 2:
        admin_panel()
        st.stop()

st.title("🏆 CPC Club Contest Spring 2026")

st.markdown("""
### 🏅 Prize Pool
- 🥇 1st: BDT 5000
- 🥈 2nd: BDT 2500
- 🥉 3rd: BDT 1000  
🎖 Top 20 get certificates

### 🎁 Facilities
- Free Jersey
- Free Lunch
- Surprise Gift
- All accessories provided by authority
""")

if st.button("Register / Login"):
    name, email = google_login()

    st.success(f"Logged in as {name}")

    row = c.execute("SELECT paid FROM users WHERE email=?", (email,)).fetchone()
    if row and row[0] == 1:
        st.info("✅ Status: PARTICIPANT")
        st.stop()

    student_id = st.text_input("Student ID (xxx-xx-xxx)")
    if not re.match(r"^\d{3}-\d{2}-\d{3}$", student_id):
        st.warning("Invalid ID format")
        st.stop()

    st.markdown("""
### 💳 Payment Breakdown (BDT 4000)
- Physics Lab Contest: 1000
- Structure Programming Lab Contest: 1500
- Electrical Circuit Lab Contest: 1500
""")

    if bkash_payment(email):
        c.execute("REPLACE INTO users VALUES (?,?,?,?,?,?)",
                  (email, name, student_id, 1, "", ""))
        conn.commit()
        st.success("🎉 Payment Successful! You are now a participant.")
        st.balloons()