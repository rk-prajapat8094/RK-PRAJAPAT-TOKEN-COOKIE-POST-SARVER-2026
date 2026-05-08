import streamlit as st
import time
import threading
import requests
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="RK KRISHNA BRAND", page_icon="🫅", layout="wide")

# Uptime calculation
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()

if 'logs' not in st.session_state:
    st.session_state.logs = []

if 'running' not in st.session_state:
    st.session_state.running = False

def get_uptime():
    diff = datetime.now() - st.session_state.start_time
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

# CSS Load (External file link logic)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# UI Header
st.markdown('<div class="main-header"><h1>🫅 FB E2EE AUTOMATION</h1><p>Made by RK KRISHNA BRAND</p></div>', unsafe_allow_html=True)

# Sidebar for Stats
st.sidebar.title("📊 Server Stats")
st.sidebar.info(f"⏱️ Uptime: {get_uptime()}")
status = "🟢 Running" if st.session_state.running else "🔴 Stopped"
st.sidebar.markdown(f"**Status:** {status}")

# Input Fields
col1, col2 = st.columns(2)
with col1:
    cookie = st.text_input("Enter Facebook Cookie", type="password")
    chat_id = st.text_input("Enter Target Chat ID")
with col2:
    message = st.text_input("Enter Your Message")
    delay = st.number_input("Delay (Seconds)", min_value=1, value=30)

# Start/Stop Buttons
btn_col1, btn_col2 = st.columns(2)
if btn_col1.button("🚀 START SERVER", use_container_width=True):
    if cookie and chat_id:
        st.session_state.running = True
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Server Started Successfully!")
    else:
        st.error("❌ Missing Details!")

if btn_col2.button("⏹️ STOP SERVER", use_container_width=True):
    st.session_state.running = False
    st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🛑 Server Stopped.")

# Long Console Log
st.markdown("### 🖥️ Live Console Log")
log_box = st.empty()

# Automation Logic
if st.session_state.running:
    # यहाँ आप अपना संदेश भेजने का लूप चला सकते हैं
    st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Sending msg to {chat_id}...")
    # requests.post(...) logic goes here

# Display Logs
log_text = "\n".join(st.session_state.logs[::-1])
log_box.text_area("", value=log_text, height=300, label_visibility="collapsed")
