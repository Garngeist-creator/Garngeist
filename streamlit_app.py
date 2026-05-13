import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- SYSTEM-SETUP ---
st.set_page_config(page_title="ThreadMate | Garngeist KI", page_icon="🧶", layout="wide")

# CSS für das "Garn-Feeling"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# Daten-Speicher initialisieren
if 'inventory' not in st.session_state:
    st.session_state.inventory = {"Stahlwolle": 0, "Nutzhanf": 3, "Vulkan-Garn": 0}
if 'log' not in st.session_state:
    st.session_state.log = []

# --- DIE PERSÖNLICHKEIT DES GARNGEISTS ---
def garngeist_reaktion(puls, schritte):
    if puls > 140:
        return "⚠️ DEIN PULS! Du überdrehst die Spindel! Atme, oder ich sehe zu, wie dein Faden reißt."
    elif schritte < 300:
        return "💤 Erbärmlich. Deine Lebensfäden hängen schlaff herunter. Beweg dich!"
    elif puls < 60:
        return "🌑 Dein Puls ist so ruhig... fast wie im Grab. Bist du noch da?"
    else:
        return "🧶 Ich beobachte das Muster deines Lebens. Web weiter, Mensch."

# --- HEADER ---
st.title("🧶 ThreadMate: Garngeist v1.0")
st.write("---")

# --- HAUPTBEREICH: BIOMETRIE ---
col1, col2, col3 = st.columns(3)

with col1:
    puls = st.slider("Aktueller Puls (BPM)", 40, 200, 75)
    st.metric("Herzschlag", f"{puls} BPM")

with col2:
    schritte = st.number_input("Schritte heute", 0, 50000, 1250)
    st.metric("Schritte", f"{schritte}")

with col3:
    st.subheader("Garngeist-Status")
    msg = garngeist_reaktion(puls, schritte)
    st.info(msg)

# --- SPIEL-MECHANIK: ITEM FUND ---
st.write("---")
if st.button("🎁 Umgebung nach Ressourcen scannen"):
    fund = random.choice(["Stahlwolle", "Nutzhanf", "Vulkan-Garn", "Nichts"])
    if fund != "Nichts":
        st.session_state.inventory[fund] += 1
        st.success(f"Gefunden: 1x {fund}! Dein Gewebe wird stärker.")
    else:
        st.warning("Nichts als Staub in den Windungen.")

# --- INVENTAR & DATEN-KAPITAL ---
c1, c2 = st.columns([1, 2])

with c1:
    st.subheader("📦 Ressourcen")
    for item, menge in st.session_state.inventory.items():
        st.write(f"**{item}:** {menge}")

with c2:
    st.subheader("💰 Dein Daten-Kapital (Vault)")
    if st.button("Snapshot für Investor sichern"):
        entry = {"Zeit": datetime.now().strftime("%H:%M"), "Puls": puls, "Schritte": schritte}
        st.session_state.log.append(entry)
        st.toast("Datenpunkt verschlüsselt gesichert.")
    
    if st.session_state.log:
        st.table(pd.DataFrame(st.session_state.log))

# --- MONETARISIERUNG (ANONYM) ---
st.write("---")
st.subheader("💎 Unterstützung & Exit-Strategie")
st.write("Sende Krypto-Unterstützung direkt in den Vault (Pfändungssicher):")
st.code("HIER_DEINE_WALLET_ADRESSE_EINTRAGEN", language="text")
st.caption("Dieses Kapital wird für die Gründung der Wyoming LLC verwendet.")
