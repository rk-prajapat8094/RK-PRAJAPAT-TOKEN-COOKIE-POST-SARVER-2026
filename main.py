from flask import Flask, render_template_string, request, jsonify
import threading
import time
import requests
import random
from datetime import datetime
import pytz

app = Flask(__name__)

ist = pytz.timezone('Asia/Kolkata')
RANDOM_ID = random.randint(1000, 9999)
STOP_TOKEN = f"RK_PRAJAPAT_{RANDOM_ID}"
DEPLOY_TIME = datetime.now(ist).strftime("%d %b, %I:%M %p")

bot_status = {
    "running": False,
    "logs": [],
    "sent_count": 0,
    "failed_count": 0,
    "active_connections": 0,
    "start_time": None
}

def add_log(status, uid="N/A", msg="N/A"):
    timestamp = datetime.now(ist).strftime("%I:%M:%S %p")
    bot_status["logs"].append({"time": timestamp, "uid": uid, "msg": msg, "status": status})
    if len(bot_status["logs"]) > 15: bot_status["logs"].pop(0)

def universal_spammer(method, target_id, auth_list, messages, delay, hater_name):
    bot_status["running"] = True
    bot_status["start_time"] = datetime.now(ist)
    bot_status["active_connections"] += 1
    
    idx = 0
    while bot_status["running"]:
        try:
            auth_val = auth_list[idx % len(auth_list)].strip()
            message = f"{hater_name} {messages[idx % len(messages)].strip()}"
            
            if method == 'token':
                url = f"https://graph.facebook.com/v17.0/{target_id}/comments"
                response = requests.post(url, data={'message': message, 'access_token': auth_val})
            else:
                headers = {'cookie': auth_val, 'user-agent': 'Mozilla/5.0'}
                url = f"https://mbasic.facebook.com/comment/replies/?ft_ent_identifier={target_id}"
                response = requests.post(url, headers=headers, data={'comment_text': message})
            
            if response.status_code == 200 or response.ok:
                bot_status["sent_count"] += 1
                add_log(f"SENT VIA {method.upper()}", uid=target_id, msg=message)
            else:
                bot_status["failed_count"] += 1
                add_log(f"{method.upper()} ERROR", uid=target_id)
            
            idx += 1
            time.sleep(int(delay))
        except:
            time.sleep(5)
    bot_status["active_connections"] -= 1

@app.route('/')
def index():
    return render_template_string(open('index.html').read(), deploy_time=DEPLOY_TIME, stop_token=STOP_TOKEN)

@app.route('/start', methods=['POST'])
def start():
    if bot_status["running"]: return "Running", 200
    method = request.form.get('method')
    t_id = request.form.get('targetID')
    auth_list = request.form.get('authData').splitlines()
    msgs = request.files.get('msgFile').read().decode().splitlines()
    delay = request.form.get('delay', 20)
    h_name = request.form.get('haterName', '')
    threading.Thread(target=universal_spammer, args=(method, t_id, auth_list, msgs, delay, h_name)).start()
    return "Started", 200

@app.route('/stop', methods=['POST'])
def stop():
    if request.form.get('stopToken') == STOP_TOKEN:
        bot_status["running"] = False
        return "Stopped", 200
    return "Wrong Token", 403

@app.route('/get-status')
def get_status():
    uptime = "0d 0h 0m"
    if bot_status["start_time"]:
        diff = datetime.now(ist) - bot_status["start_time"]
        uptime = f"{diff.days}d {diff.seconds//3600}h {(diff.seconds%3600)//60}m"
    return jsonify({"sent": bot_status["sent_count"], "failed": bot_status["failed_count"], "active": bot_status["active_connections"], "uptime": uptime, "logs": bot_status["logs"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
