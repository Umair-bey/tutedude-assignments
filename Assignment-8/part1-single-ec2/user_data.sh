#!/bin/bash

# Install Python
yum update -y
yum install -y python3 python3-pip

# --- SETUP FLASK BACKEND (Port 5000) ---
mkdir -p /opt/backend
cat > /opt/backend/app.py <<'PYEOF'
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello from Flask Backend on Port 5000!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
PYEOF
pip3 install flask
nohup python3 /opt/backend/app.py > /var/log/flask.log 2>&1 &

# --- SETUP "EXPRESS" FRONTEND (Actually a Python script to save time) ---
mkdir -p /opt/frontend
cat > /opt/frontend/app.py <<'PYEOF'
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello from Express Frontend on Port 3000!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
PYEOF
nohup python3 /opt/frontend/app.py > /var/log/frontend.log 2>&1 &