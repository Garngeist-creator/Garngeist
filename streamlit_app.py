import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- CONFIG & DESIGN ---
st.set_page_config(page_title="Garngeist | ThreadMate", page_icon="🧶", layout="wide")

# CSS für das braune Leder/Garn-Design & Neon-Akzente
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1614; 
        color: #d9c5b2;
    }
    
    /* Metriken im Leder-Stil */
    div[data-testid="stMetricValue"] {
        background-color: #2b231f;
        border: 2px solid #8c6a56;
        border-radius: 10px;
        color: #f2e8df !important;
    }

    /* Neon-Blauer Glow für Status-Texte */
    .glow-text {
        color: #00d4ff;
        text-shadow: 0px 0px 10px #00d4ff;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }

    /* Chat-Bereich */
    .stChatMessage {
        background-color: #261f1c;
        border-radius: 15px;
        border: 1px solid #594539;
    }

    /* Custom Buttons */
    .stButton>button {
        background-color: #3d302a;
        color: #f2e8df;
        border: 1px solid #8c6a56;
        border-radius: 5px;
        width: 100%;
    }
    .stButton>button:hover {
        border-color: #00d4ff;
        color: #00d4ff;
        box-shadow: 0px 0px 10px #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DEIN BILD-LINK (AUTOMATISIERT) ---
# Wir nutzen den Raw-Link, damit das Bild direkt in der App erscheint
AVATAR_URL = "https://raw.githubusercontent.com/Garngeist-creator/Garngeist/main/Gemini_Generated_Image_k17wvxk17wvxk17w.png"

# --- INITIALISIERUNG ---
if 'items' not in st.session_state:
    st.session_state.items = {"Nutzhanf": 12, "Stahlwolle": 0}

# --- UI LAYOUT ---
st.title("🧶 GARNGEIST SYSTEM CONTROL")

col1, col2 = st.columns([1, 2])

with col1:
    # Hier wird dein Charakter angezeigt
    st.image(AVATAR_URL, use_container_width=True)
    
    st.subheader("📡 Biometrie")
    puls = st.slider("Herzschlag (BPM)", 40, 200, 72)
    schritte = st.number_input("Tages-Schritte", 0, 30000, 4500)

with col2:
    # Dynamische Status-Meldung
    status_msg = "GEWEBE STABIL" if puls < 140 else "🚨 KRITISCHER ZUSTAND"
    st.markdown(f"### <span class='glow-text'>{status_msg}</span>", unsafe_allow_html=True)
    
    # Der Garngeist-Chat (Persönlichkeit)
    with st.chat_message("assistant", avatar="🧶"):
        if puls > 140:
            st.write("Mensch! Dein Puls rast. Willst du, dass dein Faden reißt? Setz dich hin!")
        else:
            st.write("Dein Rhythmus ist akzeptabel, Weber. Das braune Garn hält den Belastungen stand.")

    st.divider()
    
    # Handlungen
    st.subheader("🛠️ Web-Operationen")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🧶 Nutzhanf sammeln"):
            st.session_state.items["Nutzhanf"] += 1
            st.toast("Ressource gesichert.")
    with c2:
        st.button("🛡️ Vault sichern")
    with c3:
        st.button("⚙️ System-Upgrade")

# --- SIDEBAR (INVENTAR) ---
st.sidebar.header("📦 Material-Lager")
st.sidebar.metric("Nutzhanf", f"{st.session_state.items['Nutzhanf']} m")
st.sidebar.metric("Stahlwolle", f"{st.session_state.items['Stahlwolle']} m")
st.sidebar.write("---")
st.sidebar.info("Status: Anonymität durch Krypto-Vault gewährt.")
