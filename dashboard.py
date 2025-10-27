import streamlit as st
import requests

st.title("🔒 Team 9 AI Data Redactor - POPIA, FICA, GDPR, PCI DSS!")

user_input = st.text_area("Enter text containing sensitive info:")

if st.button("Redact"):
    res = requests.post("http://localhost:8000/redact", json={"text": user_input})
    if res.status_code == 200:
        redacted = res.json()["redacted_text"]
        st.subheader("✅ Redacted Text")
        st.write(redacted)
    else:
        st.error("Error communicating with backend.")
