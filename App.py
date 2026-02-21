import streamlit as st
import base64

st.set_page_config(page_title="Spengler Fachregeln App", layout="wide")

# Funktion zum Anzeigen der PDF-Seite
def display_pdf_page(file, page_number):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Der Parameter #page=X springt direkt zur Seite
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#page={page_number}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- APP STRUKTUR ---
st.title("⚒️ Fachregel-Navigator Klempnerhandwerk")

# Navigation
st.sidebar.header("Kapitelauswahl")
kapitel = st.sidebar.radio("Thema wählen:", [
    "3. Werkstoffe", 
    "4. Dachentwässerung", 
    "5. Metalldächer",
    "12. Außenwandbekleidung"
])

# Zuordnung der Startseiten aus deiner mitch1.pdf
seiten_index = {
    "3. Werkstoffe": 18,
    "4. Dachentwässerung": 33,
    "5. Metalldächer": 82,
    "12. Außenwandbekleidung": 158
}

# TEXT-ANALYSE BEREICH (Oben)
st.subheader(f"Analyse zu: {kapitel}")

if kapitel == "3. Werkstoffe":
    st.write("""
    **Wichtige Eckpunkte aus diesem Kapitel:**
    - Übersicht der Metalle: Aluminium, Kupfer, Titanzink, Edelstahl.
    - Korrosionsschutz: Achte auf die Kontaktkorrosion (z.B. Kupfer nicht über verzinktem Stahl).
    - Längenausdehnung: Wichtige Koeffizienten für die Planung der Dehnungsausgleicher.
    """)
    [attachment_0](attachment)

elif kapitel == "4. Dachentwässerung":
    st.write("""
    **Wichtige Eckpunkte aus diesem Kapitel:**
    - Dimensionierung von Dachrinnen und Regenfallrohren.
    - Befestigungsabstände für Rinnenhalter.
    - Traufblechausbildungen und Überlappungen.
    """)
    

# PDF BEREICH (Unten)
st.divider()
st.subheader("📄 Originale PDF-Seite aus dem Regelwerk")

# WICHTIG: Die Datei muss im selben Ordner liegen wie das Skript und "mitch1.pdf" heißen
try:
    display_pdf_page("mitch1.pdf", seiten_index[kapitel])
except FileNotFoundError:
    st.error("Datei 'mitch1.pdf' nicht im Ordner gefunden. Bitte stelle sicher, dass der Dateiname stimmt!")
