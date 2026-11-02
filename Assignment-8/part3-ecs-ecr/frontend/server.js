const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

// Note: We are pointing to the ALB root, because the ALB routes it to the backend
const ALB_DNS = process.env.ALB_DNS || 'localhost';
const BACKEND_URL = `http://${ALB_DNS}/api/`; // Added trailing slash

app.get('/', (req, res) => {
    res.send('<h1>Hello from the Express Frontend running in ECS Fargate!</h1><br><a href="/test">Click here to test connection to the Flask Backend via ALB</a>');
});

app.get('/test', async (req, res) => {
    try {
        const response = await axios.get(BACKEND_URL);
        res.send(`<h1>Success!</h1><p>Backend says: <strong>${response.data}</strong></p>`);
    } catch (error) {
        res.send(`<h1>Error</h1><p>Could not connect: ${error.message}</p>`);
    }
});

app.listen(PORT, () => console.log('Frontend running on port 3000'));