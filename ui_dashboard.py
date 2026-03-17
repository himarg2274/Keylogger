import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Cybersecurity Keylogger Simulation", layout="wide")

st.title("🔐 Keylogging Attack & Detection Dashboard")

st.write("This dashboard demonstrates a cybersecurity simulation of a keylogging attack and ML-based detection system.")

# ------------------ BUTTONS ------------------ #

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶ Start Keylogger"):
        subprocess.Popen(["python", "keylogger.py"])
        st.success("Keylogger started")

with col2:
    if st.button("🛑 Stop Keylogger"):
        st.warning("Press ESC in the keylogger terminal to stop logging")

with col3:
    import subprocess
import streamlit as st

if st.button("🔍 Run Detector"):
    subprocess.Popen(["python", "detector.py"])
    st.success("Detector started! Check the terminal for alerts.")

# ------------------ VIEW LOGS ------------------ #

st.header("📄 Logs")

log_option = st.selectbox(
    "Select log file",
    ["keylogs.txt", "wordlogs.txt", "summary.txt", "system.log"]
)

if st.button("View Log"):
    if os.path.exists(log_option):
        with open(log_option, "r") as f:
            st.text(f.read())
    else:
        st.error("File not found")

# ------------------ DATASET VIEW ------------------ #



# ------------------ MODEL INFO ------------------ #

