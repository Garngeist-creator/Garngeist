import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- SETUP ---
st.set_page_config(page_title="Garngeist KI", page_icon="🧶")

if 'vault' not in st.session_state:
    st.session_state.vault = []

# --- DIE KI LOGIK ---
def garngeist_spricht(puls):
    if puls > 130:
        return "🚨 PULS ZU HOCH! Atme tief, oder dein Lebensfaden reißt heute noch!"
    return "🧶 Ich beobachte dich. Web gefälligst ordentlich weiter."

# --- OBERFLÄCHE ---
st.title("🧶 Garngeist: Dein biometrisches Kapital")

puls = st.sidebar.slider("Simulierter Puls (BPM)", 40, 180, 75)
st.chat_message("assistant", avatar="🧶").write(f"**Garngeist:** {garngeist_spricht(puls)}")

if st.button("📊 Daten-Snapshot für Investor sichern"):
    st.session_state.vault.append({"Zeit": datetime.now().strftime("%H:%M:%S"), "Puls": puls})
    st.success("Daten im anonymen Vault gesichert!")

if st.session_state.vault:
    st.dataframe(pd.DataFrame(st.session_state.vault))

# --- GELD EMPFANGEN ---
st.divider()
st.subheader("💎 Anonyme Unterstützung")
st.code("DEINE_KRYPTO_ADRESSE_HIER", language="text")
st.caption("Direkt-Zahlung ohne deutsches Bankkonto.")
