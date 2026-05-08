import streamlit as st
import time
from datetime import datetime
import pandas as pd

# Page Config
st.set_page_config(page_title="RK KRISHNA BRAND ADMIN", layout="wide")

# Session State for tracking
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()
if 'total_msgs' not in st.session_state:
    st.session_state.total_msgs = 0
if 'failed_msgs' not in st.session_state:
    st.session_state.failed_msgs = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# CSS for styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Dashboard Header
st.markdown('<div class="main-header"><h1>🫅 RK KRISHNA BRAND OFFICIAL DASHBOARD</h1></div>', unsafe_allow_html=True)

# Metrics Row
uptime = str(datetime.now() - st.session_state.start_time).split('.')[0]
col1, col2, col3, col4 = st.columns(4)
col1.metric("⏱️ Uptime", uptime)
col2.metric("👥 Active Users", "1") # Single user for now
col3.metric("✅ Sent Messages", st.session_state.total_msgs)
col4.metric("❌ Failed Messages", st.session_state.failed_msgs, delta_color="inverse")

# Controls
st.sidebar.title("Settings")
delay = st.sidebar.slider("Delay (Seconds)", 5, 300, 30)
stop_btn = st.sidebar.button("⏹️ Stop All Tasks")

# Main Interface
c1, c2 = st.columns([1, 2])

with c1:
    st.subheader("🚀 Start Automation")
    cookie = st.text_input("Cookie", type="password")
    target = st.text_input("Target ID")
    message = st.text_area("Message")
    if st.button("Launch Attack"):
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 Attack Launched on {target}")
        # Logic to call your app.py functions can be added here silently

with c2:
    st.subheader("🖥️ Live Console Output")
    # Long Console Logic
    log_content = "\n".join(st.session_state.logs[-50:][::-1])
    st.text_area("Console", value=log_content, height=400, label_visibility="collapsed")

# Auto-Refresh Logic
time.sleep(2)
st.rerun()
