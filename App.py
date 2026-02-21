import streamlit as st
import PyPDF2

# Funktion zum Laden der PDF
def load_pdf():
    with open("path_to_your_pdf_file.pdf", "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return reader.pages

# Funktion zum Extrahieren von Text aus PDF
def extract_text_from_pdf(page):
    return page.extract_text()

# Kategorien und Unterkategorien
categories = {
    "Einführung": "Die vorliegende Richtlinie bildet die Zusammenfassung des aktuellen Sachstands im Klempnerhandwerk ab.",
    "Geltungsbereich": "Diese Richtlinien gelten für die Ausführung von Deckungen von Dächern und Bekleidungen von Fassaden.",
    "Begriffe": "Definitionen wichtiger Fachbegriffe im Klempnerhandwerk.",
    "Werkstoffe": {
        "Allgemeines": "Eine ausreichende Produktkennzeichnung ist notwendig.",
        "Bleche, Bänder und Bauteile": {
            "Aluminium": "Informationen zu Aluminium blechen...",
            "Blei": "Details zu Bleiblechen...",
            # Weitere Materialkategorien hier
        }
    },
    # Weitere Kategorien hier...
}

# Streamlit App Layout
st.title("Klempner Fachregeln")
st.sidebar.title("Navigation")

# Auswahl der Kategorien
selected_category = st.sidebar.selectbox("Wähle eine Kategorie:", list(categories.keys()))

# Anzeige der ausgewählten Kategorie
if selected_category in categories:
    content = categories[selected_category]
    if isinstance(content, dict):
        selected_subcategory = st.selectbox("Wähle eine Unterkategorie:", list(content.keys()))
        content = content[selected_subcategory]
    st.write(content)

# Suchfunktion
st.header("Suchfunktion")
search_term = st.text_input("Suchbegriff eingeben:")
if search_term:
    pages = load_pdf()
    results = []
    for page in pages:
        text = extract_text_from_pdf(page)
        if search_term.lower() in text.lower():
            results.append(text)
    if results:
        st.write("Suchergebnisse:")
        for result in results:
            st.write(result)
    else:
        st.write("Keine Ergebnisse gefunden.")

# Original PDF Anzeige
st.header("Original PDF")
with open("path_to_your_pdf_file.pdf", "rb") as f:
    st.download_button(label="Lade die PDF herunter", data=f, file_name="klempner_fachregeln.pdf")
