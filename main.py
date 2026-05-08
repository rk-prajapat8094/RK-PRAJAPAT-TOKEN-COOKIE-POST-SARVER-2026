import os
import time
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- प्रोफेशनल UI डिजाइन ---
HTML_DESIGN = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FB E2EE BY RK-PRAJAPAT</title>
    <style>
        body { background-color: #0d1117; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 0 0 20px 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        .container { max-width: 500px; margin: 30px auto; padding: 20px; background: #161b22; border: 1px solid #30363d; border-radius: 15px; }
        input { width: 90%; padding: 12px; margin: 10px 0; background: #0d1117; border: 1px solid #58a6ff; color: white; border-radius: 8px; }
        button { width: 100%; padding: 15px; background: #238636; border: none; color: white; font-weight: bold; border-radius: 8px; cursor: pointer; transition: 0.3s; }
        button:hover { background: #2ea043; }
        .footer { margin-top: 50px; font-size: 12px; color: #8b949e; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🫅 FB E2EE AUTOMATION</h1>
        <p>Made by RK KRISHNA BRAND</p>
    </div>
    <div class="container">
        <form action="/start" method="post">
            <input type="text" name="cookie" placeholder="Paste Facebook Cookie" required>
            <input type="text" name="chat_id" placeholder="Enter Target Chat ID" required>
            <input type="text" name="msg" placeholder="Enter Your Message" required>
            <input type="number" name="delay" value="30" placeholder="Delay in Seconds">
            <button type="submit">▶️ START AUTOMATION</button>
        </form>
    </div>
    <div class="footer">© 2025 RK-PRAJAPAT | ALL RIGHTS RESERVED</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_DESIGN)

@app.route('/start', methods=['POST'])
def start():
    cookie = request.form.get('cookie')
    chat_id = request.form.get('chat_id')
    message = request.form.get('msg')
    delay = int(request.form.get('delay', 30))

    # यहाँ बैकएंड पर मैसेज भेजने का काम शुरू होगा
    # Note: E2EE के लिए कुकी और चैट आईडी सही होना जरूरी है
    return f"<h1>✅ Automation Started!</h1><p>Target ID: {chat_id}<br>Message will be sent every {delay} seconds.</p><a href='/'>Go Back</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
