#!/bin/bash
yum update -y
curl -sL https://rpm.nodesource.com/setup_16.x | bash -
yum install -y nodejs

mkdir -p /opt/frontend
cd /opt/frontend

cat > package.json <<'JSONEOF'
{
  "name": "frontend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": { "express": "^4.18.2", "axios": "^1.6.0" }
}
JSONEOF

cat > server.js <<'JSEOF'
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

const BACKEND_URL = 'http://__BACKEND_IP__:5000';

app.get('/', (req, res) => {
    res.send('<h1>Hello from the Express Frontend!</h1><br><a href="/api">Click here to test connection to the Flask Backend</a>');
});

app.get('/api', async (req, res) => {
    try {
        const response = await axios.get(BACKEND_URL);
        res.send(`<h1>Success!</h1><p>Backend says: <strong>${response.data}</strong></p>`);
    } catch (error) {
        res.send(`<h1>Error</h1><p>Could not connect: ${error.message}</p>`);
    }
});

app.listen(PORT, () => console.log('Frontend running on port 3000'));
JSEOF

# Replace the placeholder with the real IP injected by Terraform
sed -i "s/__BACKEND_IP__/__REAL_BACKEND_IP__/g" server.js

npm install
nohup node server.js > /var/log/express.log 2>&1 &