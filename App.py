import streamlit as st
import base64
import fitz  # PyMuPDF

# --- SEITEN-SETUP ---
st.set_page_config(page_title="Spengler Profi-App", layout="wide", page_icon="⚒️")

# --- CUSTOM DESIGN (CSS) ---
st.markdown("""
    <style>
    /* Hintergrund und Schrift */
    .stApp { background-color: #1e1e1e; color: #ffffff; }
    
    /* Karten-Design für die Texte */
    .feature-card {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 20px;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #121212 !important;
    }
    
    /* Titel-Farbe */
    h1, h2, h3 { color: #ff4b4b !important; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKTIONEN ---
def display_pdf_page(file_path, page_number):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # PDF-Viewer
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#page={page_number}" width="100%" height="850" type="application/pdf" style="border:none; border-radius: 10px;"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Fehler: {e}")

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1063/1063196.png", width=100) # Ein kleines Icon
st.sidebar.title("Regelwerks-Navigator")
kapitel_liste = {
    "Übersicht": 1,
    "3. Werkstoffe": 18,
    "4. Dachentwässerung": 33,
    "5. Metalldächer": 82,
    "12. Außenwandbekleidung": 158
}
wahl = st.sidebar.radio("Kapitel schnell ansteuern:", list(kapitel_liste.keys()))

# --- HAUPTBEREICH ---
col1, col2 = st.columns([1, 2])

with col1:
    st.title("⚒️ Spengler-App")
    st.markdown("### Schnellsuche")
    search_query = st.text_input("", placeholder="Begriff eingeben...")
    
    st.divider()

    if search_query:
        # Suchlogik
        st.write(f"Ergebnisse für: **{search_query}**")
        # Hier nutzen wir eine vereinfachte Liste für die Demo
        st.info("Suche in mitch1.pdf läuft...")
        # (Hier die Suchfunktion aus dem letzten Schritt einfügen)
    else:
        # Info-Karten je nach Kapitel
        if wahl == "3. Werkstoffe":
            st.markdown(f"""<div class="feature-card">
                <h3>Kapitel 3: Werkstoffe</h3>
                <p><b>Wichtig:</b> Kontaktkorrosion beachten!<br>
                Kupfer > verzinkter Stahl = ❌ Verboten<br>
                Längenausdehnung Tabelle 3.1 prüfen.</p>
                </div>""", unsafe_allow_html=True)
            

        elif wahl == "4. Dachentwässerung":
            st.markdown(f"""<div class="feature-card">
                <h3>Kapitel 4: Entwässerung</h3>
                <p><b>Wichtig:</b> Rinnengefälle & Halterabstände.<br>
                Überprüfung der Notüberläufe nach DIN EN 12056-3.</p>
                </div>""", unsafe_allow_html=True)
            [attachment_0](attachment)
            
        else:
            st.markdown(f"""<div class="feature-card">
                <h3>Willkommen!</h3>
                <p>Wähle links ein Kapitel oder nutze die Suche oben, um direkt in die Fachregeln zu springen.</p>
                </div>""", unsafe_allow_html=True)

with col2:
    # PDF Anzeige
    st.markdown("### Dokumenten-Ansicht")
    display_pdf_page("mitch1.pdf", kapitel_liste[wahl])
