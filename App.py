import streamlit as st
import base64
import fitz  # PyMuPDF für die Suche

# --- SEITEN-SETUP ---
st.set_page_config(page_title="Spengler Fachregeln", layout="wide", page_icon="⚒️")

# --- CUSTOM DESIGN (Anthrazit & Bronze) ---
st.markdown("""
    <style>
    .stApp { background-color: #1A1A1A; color: #E0E0E0; }
    section[data-testid="stSidebar"] { background-color: #262626 !important; border-right: 2px solid #CD7F32; }
    
    /* Große Bronze-Buttons */
    div.stButton > button {
        background-color: #2C2C2C;
        color: #CD7F32;
        border: 2px solid #CD7F32;
        border-radius: 12px;
        padding: 15px 20px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover { background-color: #CD7F32; color: #1A1A1A; border: 2px solid #ffffff; }
    
    h1, h2, h3 { color: #CD7F32 !important; }
    .stTextInput > div > div > input { background-color: #2C2C2C; color: white; border: 1px solid #CD7F32; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKTIONEN ---

def display_pdf_page(file_path, page_number):
    """Zeigt die PDF-Seite in einem eleganten Frame an."""
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#page={page_number}" width="100%" height="900" style="border: 2px solid #CD7F32; border-radius: 15px;"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except:
        st.error("Datei 'mitch1.pdf' nicht gefunden. Bitte lade sie hoch!")

def search_pdf(file_path, query):
    """Durchsucht das Dokument nach Begriffen."""
    results = []
    if query:
        try:
            doc = fitz.open(file_path)
            for page_num in range(len(doc)):
                text = doc[page_num].get_text("text")
                if query.lower() in text.lower():
                    results.append(page_num + 1)
            doc.close()
        except: pass
    return results

# --- LOGIK ---

if 'page' not in st.session_state:
    st.session_state.page = 1

st.title("⚒️ SPENGLER FACHREGELN")

# Suchleiste
search_query = st.text_input("🔍 Dokument durchsuchen:", placeholder="z.B. Falz, Traufe, Kupfer...")

col_nav, col_pdf = st.columns([1, 2])

with col_nav:
    st.markdown("### Navigation")
    
    # Große Schaltflächen
    if st.button("🏠 Startseite"): st.session_state.page = 1
    if st.button("🧪 3. Werkstoffe"): st.session_state.page = 18
    if st.button("💧 4. Dachentwässerung"): st.session_state.page = 33
    if st.button("🏠 5. Metalldächer"): st.session_state.page = 82
    if st.button("🧱 12. Außenwände"): st.session_state.page = 158

    # Suchergebnisse anzeigen
    if search_query:
        st.markdown("---")
        st.subheader("Suchergebnisse")
        found_pages = search_pdf("mitch1.pdf", search_query)
        if found_pages:
            st.success(f"{len(found_pages)} Treffer gefunden.")
            selected_res = st.selectbox("Seite wählen:", found_pages)
            if st.button("Zu Seite springen"):
                st.session_state.page = selected_res
        else:
            st.warning("Keine Treffer.")

with col_pdf:
    st.subheader(f"Aktuelle Ansicht: Seite {st.session_state.page}")
    display_pdf_page("mitch1.pdf", st.session_state.page)
