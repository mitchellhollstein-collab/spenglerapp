import streamlit as st
import fitz  # PyMuPDF
import base64

# Konfiguration der Seite
st.set_page_config(page_title="Spengler Fachregeln", layout="wide")

# Styling für das mobile Design (Dark Mode & Große Buttons)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .search-box {
        position: sticky;
        top: 0;
        z-index: 1000;
        background-color: #0e1117;
        padding: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_pdf():
    return fitz.open("mitch1.pdf")

doc = load_pdf()

# Titel & Suche
st.title("👷 Spengler Fachregeln")
query = st.text_input("Suchen in 203 Seiten...", placeholder="z.B. Traufblech, Rinnenhalter, Zink")

# Hauptmenü (Kategorien)
if not query:
    st.subheader("Kategorien")
    col1, col2 = st.columns(2)
    
    categories = {
        "Werkstoffe": 5, 
        "Dachentwässerung": 35, 
        "Metalldächer": 85, 
        "Fassade": 140, 
        "Löten/Praxis": 180
    }
    
    for i, (name, page) in enumerate(categories.items()):
        if i % 2 == 0:
            if col1.button(name):
                st.session_state.page = page
        else:
            if col2.button(name):
                st.session_state.page = page

# Suchlogik
if query:
    st.subheader(f"Suchergebnisse für '{query}':")
    results = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if query.lower() in text.lower():
            results.append(page_num)
    
    if results:
        for res in results[:10]: # Zeige die ersten 10 Treffer
            if st.button(f"Gefunden auf Seite {res + 1}"):
                st.session_state.page = res
    else:
        st.error("Nichts gefunden. Versuche einen anderen Begriff.")

# Anzeige (Option C: Text + PDF Seite)
if 'page' in st.session_state:
    p_num = st.session_state.page
    page = doc.load_page(p_num)
    
    st.divider()
    st.subheader(f"Seite {p_num + 1}")
    
    # Text-Extrakt
    with st.expander("Text-Inhalt anzeigen"):
        st.write(page.get_text())
    
    # PDF-Seite als Bild anzeigen
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # Höhere Auflösung
    img_data = pix.tobytes("png")
    st.image(img_data, use_column_width=True)
