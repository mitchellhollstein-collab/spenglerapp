import streamlit as st
import base64
import fitz  # PyMuPDF

# --- SEITEN-SETUP ---
st.set_page_config(page_title="Spengler Fachregeln", layout="wide", page_icon="⚒️")

# --- CUSTOM DESIGN (CSS für Anthrazit & Bronze) ---
st.markdown("""
    <style>
    /* Hintergrund der gesamten App */
    .stApp {
        background-color: #1A1A1A;
        color: #E0E0E0;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #262626 !important;
        border-right: 2px solid #CD7F32;
    }

    /* Große, moderne Buttons (Schaltflächen) */
    div.stButton > button {
        background-color: #2C2C2C;
        color: #CD7F32;
        border: 2px solid #CD7F32;
        border-radius: 12px;
        padding: 20px 24px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
        text-align: left;
        margin-bottom: 10px;
    }
    
    div.stButton > button:hover {
        background-color: #CD7F32;
        color: #1A1A1A;
        border: 2px solid #ffffff;
        transform: scale(1.02);
    }

    /* Überschriften in Bronze */
    h1, h2, h3 {
        color: #CD7F32 !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Suchleiste Styling */
    .stTextInput > div > div > input {
        background-color: #2C2C2C;
        color: white;
        border: 1px solid #CD7F32;
    }

    /* Info-Boxen */
    .stAlert {
        background-color: #2C2C2C;
        border: 1px solid #CD7F32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKTIONEN ---
def display_pdf_page(file_path, page_number):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#page={page_number}" width="100%" height="900" type="application/pdf" style="border: 2px solid #CD7F32; border-radius: 15px;"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.error("Bitte stelle sicher, dass 'mitch1.pdf' im Ordner liegt.")

# --- HAUPTBEREICH ---
st.title("⚒️ SPENGLER FACHREGELN")

# Obere Reihe: Suche
search_query = st.text_input("🔍 Schnellsuche im Regelwerk:", placeholder="Begriff eingeben (z.B. Falz, Rinne, Zink)...")

col_nav, col_pdf = st.columns([1, 2])

# Navigation über große Schaltflächen
with col_nav:
    st.markdown("### Kapitel")
    
    # Wir nutzen eine Session State Variable, um die Seite zu merken
    if 'page' not in st.session_state:
        st.session_state.page = 1

    if st.button("📄 Startseite / Vorwort"):
        st.session_state.page = 1
    
    if st.button("🧪 3. Werkstoffe"):
        st.session_state.page = 18
        
    if st.button("💧 4. Dachentwässerung"):
        st.session_state.page = 33
        
    if st.button("🏠 5. Metalldächer"):
        st.session_state.page = 82
        
    if st.button("🧱 12. Außenwände"):
        st.session_state.page = 158

    st.divider()
    st.info("Tipp: Die Seitenzahlen beziehen sich auf das offizielle ZVSHK-Dokument.")

# PDF Anzeige im rechten Bereich
with col_pdf:
    if search_query:
        st.subheader(f"Sucher
