@'
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-service:3000")

@app.route('/')
def home():
    try:
        r = requests.get(f"{BACKEND_URL}/api", timeout=5)
        data = r.json()
    except Exception as e:
        data = {"message": f"Backend not reachable: {e}", "status": "error"}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'@ | Set-Content frontend\app.py