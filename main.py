import os
import time
import requests
from flask import Flask, request, render_template, jsonify
import threading

app = Flask(__name__)

# डेटा स्टोर करने के लिए
data_store = {
    "botStatus": "🔴 STOPPED",
    "uptime": "00d 00h 00m",
    "sentCount": 0,
    "failedCount": 0,
    "mode": "N/A",
    "targetId": "N/A",
    "prefix": "HATERS",
    "cookies": 0,
    "messages": 0,
    "delay": 0
}

logs = []
stop_event = threading.Event()

def add_log(msg):
    logs.append(msg)
    if len(logs) > 30: logs.pop(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_bot():
    global stop_event
    stop_event.clear()
    
    # फॉर्म से डेटा लेना
    mode = request.form.get('mode')
    target_id = request.form.get('targetID')
    delay = int(request.form.get('delay'))
    
    # फाइल हैंडलिंग का लॉजिक यहाँ आएगा
    add_log(f"🚀 Task Started for ID: {target_id}")
    data_store["botStatus"] = "🟢 RUNNING"
    
    return "Started"

@app.route('/get-status')
def get_status():
    return jsonify(data_store)

@app.route('/get-logs')
def get_logs():
    return jsonify(logs)

@app.route('/get-session-id')
def session_id():
    return jsonify({"sessionId": "DEVIL-PRO-999"})

if __name__ == '__main__':
    # Render के लिए पोर्ट सेटिंग
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
