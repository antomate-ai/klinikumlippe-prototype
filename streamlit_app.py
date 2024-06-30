import streamlit as st
import re

# Titel des Streamlit-Apps
st.title("Vierstellige Zahl Extrahierer")

# Eingabefeld für den Text
input_text = st.text_area("Geben Sie Ihren Text ein:")

# Funktion zur Extraktion vierstelliger Zahlen
def extract_four_digit_numbers(text):
    return re.findall(r'\b\d{4}\b', text)

# Verarbeitung des Eingabetextes
if st.button("Extrahieren"):
    extracted_numbers = extract_four_digit_numbers(input_text)
    
    if extracted_numbers:
        st.write("Extrahierte vierstellige Zahlen:")
        for number in extracted_numbers:
            st.write(number)
    else:
        st.write("Keine vierstelligen Zahlen gefunden.")

# Dieses Skript können Sie in einer Python-Umgebung mit installiertem Streamlit ausführen.
# Um das Skript zu starten, speichern Sie es in einer Datei (z.B. app.py) und führen Sie im Terminal `streamlit run app.py` aus.
