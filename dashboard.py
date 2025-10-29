import streamlit as st
import requests

# --- Page Configuration ---
st.set_page_config(
    page_title="FNB AI Data Redactor",
    page_icon="🔒",
    layout="centered",
)

# --- FNB Color Palette (Dark Mode) ---
FNB_TEAL = "#00758F"      # FNB primary teal
FNB_GOLD = "#F2A900"      # FNB accent gold
LIGHT_TEXT = "#FFFFFF"    # White text
DARK_BG = "#000000"       # Black background

# --- Custom CSS for Dark Theme Styling ---
st.markdown(f"""
    <style>
        body {{
            background-color: {DARK_BG};
        }}
        .stApp {{
            background-color: {DARK_BG};
        }}
        .main-container {{
            background-color: #111111;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            padding: 2.5em 3em;
            max-width: 700px;
            margin: 2em auto;
        }}
        h1 {{
            color: {FNB_GOLD};
            text-align: center;
            font-weight: 800;
        }}
        h4 {{
            text-align: center;
            color: {FNB_TEAL};
            font-weight: 600;
        }}
        label, p, .stMarkdown, .stTextArea label {{
            color: {LIGHT_TEXT} !important;
        }}
        textarea {{
            border: 2px solid {FNB_TEAL} !important;
            border-radius: 10px !important;
            font-size: 1rem !important;
            background-color: #222222 !important;
            color: {LIGHT_TEXT} !important;
        }}
        .stButton>button {{
            background-color: {FNB_GOLD};
            color: black;
            font-weight: 600;
            border-radius: 8px;
            border: none;
            padding: 0.6em 1.4em;
        }}
        .stButton>button:hover {{
            background-color: {FNB_TEAL};
            color: white;
        }}
        .stSubheader, .stSuccess, .stWarning, .stError {{
            color: {FNB_GOLD} !important;
        }}
    </style>
""", unsafe_allow_html=True)

# --- Main UI Container ---
with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    st.title("🔒 Team 9 AI Data Redactor")
    st.markdown("#### POPIA • FICA • GDPR • PCI DSS Compliant")

    # --- Input Box ---
    user_input = st.text_area("✍️ Enter text containing sensitive information:", height=200)

    # --- Redact Button ---
    if st.button("🔍 Redact Sensitive Data"):
        if not user_input.strip():
            st.warning("⚠️ Please enter some text before redacting.")
        else:
            with st.spinner("Redacting... please wait ⏳"):
                try:
                    res = requests.post("http://localhost:8000/redact", json={"text": user_input})
                    if res.status_code == 200:
                        redacted = res.json().get("redacted_text", "")
                        st.subheader("✅ Redacted Text")
                        st.success(redacted)
                    else:
                        st.error("❌ Error communicating with backend.")
                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Request failed: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
