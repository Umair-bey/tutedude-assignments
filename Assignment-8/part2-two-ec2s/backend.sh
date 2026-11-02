#!/bin/bash
yum update -y
yum install -y python3 python3-pip

mkdir -p /opt/backend
cat > /opt/backend/app.py <<'PYEOF'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from the Flask Backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
PYEOF

pip3 install flask
nohup python3 /opt/backend/app.py > /var/log/flask.log 2>&1 &