#!/bin/bash
set -e

# Update system and install Python & Node.js
yum update -y
yum install -y python3 python3-pip
curl -fsSL https://rpm.nodesource.com/setup_18.x | bash -
yum install -y nodejs

# --- SETUP FLASK BACKEND ---
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
# Run Flask in the background
nohup python3 /opt/backend/app.py > /var/log/flask.log 2>&1 &

# --- SETUP EXPRESS FRONTEND ---
mkdir -p /opt/frontend
cd /opt/frontend
cat > package.json <<'JSONEOF'
{
  "name": "frontend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": { "express": "^4.18.2" }
}
JSONEOF

cat > server.js <<'JSEOF'
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello from Express Frontend on Port 3000!'));
app.listen(3000, () => console.log('Frontend on 3000'));
JSEOF

npm install
# Run Express in the background
nohup node server.js > /var/log/express.log 2>&1 &