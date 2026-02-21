import streamlit as st
import base64

st.set_page_config(page_title="Spengler Fachregeln App", layout="wide")

# Funktion zum Anzeigen der PDF-Seite
def display_pdf_page(file_path, page_number):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # PDF in iframe einbetten, springt zur Seite (Index startet bei 1 für PDF-Viewer)
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#page={page_number}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Die Datei '{file_path}' wurde nicht gefunden. Bitte lade sie in das Verzeichnis hoch.")

# --- APP STRUKTUR ---
st.title("⚒️ Fachregel-Navigator Klempnerhandwerk")

# Navigation in der Sidebar
st.sidebar.header("Kapitelauswahl")
kapitel = st.sidebar.radio("Thema wählen:", [
    "3. Werkstoffe", 
    "4. Dachentwässerung", 
    "5. Metalldächer",
    "12. Außenwandbekleidung"
])

# Zuordnung der Seitenzahlen (Basierend auf deinem Dokument mitch1.pdf)
# Hinweis: PDF-Reader fangen oft bei Seite 1 an zu zählen.
seiten_index = {
    "3. Werkstoffe": 18,
    "4. Dachentwässerung": 33,
    "5. Metalldächer": 82,
    "12. Außenwandbekleidung": 158
}

# TEXT-ANALYSE BEREICH (Oben)
st.subheader(f"Wichtige Infos zu: {kapitel}")

if kapitel == "3. Werkstoffe":
    st.info("📌 **Fokus:** Materialeigenschaften und Korrosionsschutz.")
    st.write("""
    - **Metalle:** Aluminium, Kupfer, Edelstahl, Titanzink.
    - **Wichtig:** Kontaktkorrosion vermeiden! Kupfer darf niemals *vor* verzinkten Bauteilen in Fließrichtung liegen.
    - **Längenausdehnung:** Tabelle 3.1 im PDF beachten (S. 20).
    """)

elif kapitel == "4. Dachentwässerung":
    st.info("📌 **Fokus:** Bemessung und Montage von Rinnen.")
    st.write("""
    - **Rinnen:** Halbrunde und kastenförmige Rinnen nach DIN EN 612.
    - **Gefälle:** Empfehlung mind. 1mm bis 3mm pro Meter.
    - **Löten:** Kapillarspalt von 0,5mm bis 2mm einhalten.
    """)
    

elif kapitel == "5. Metalldächer":
    st.info("📌 **Fokus:** Unterkonstruktion und Belüftung.")
    st.write("""
    - **Belüftung:** Zuluft am Traufpunkt, Abluft am First.
    - **Trennlagen:** Wann ist eine strukturierte Trennlage erforderlich? (Siehe S. 85).
    """)
    

# PDF BEREICH (Unten)
st.divider()
st.subheader(f"📄 Originaldokument: Seite {seiten_index[kapitel]}")

# Hier wird die PDF angezeigt
display_pdf_page("mitch1.pdf", seiten_index[kapitel])
