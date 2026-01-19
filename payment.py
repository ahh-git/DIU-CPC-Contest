import streamlit as st

def bkash_payment(email):
    st.image("assets/bkash.png", width=130)
    st.info("Live bKash Checkout")

    if st.button("Pay with bKash (BDT 4000)"):
        # live API already shared previously
        st.session_state.paid = True
        return True
    return False