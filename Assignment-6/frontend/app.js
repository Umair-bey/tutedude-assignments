const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Backend URL is injected via env var during deployment
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/', async (req, res) => {
  let items = [];
  let error = null;
  try {
    const response = await axios.get(`${BACKEND_URL}/api/items`);
    items = response.data;
  } catch (err) {
    error = `Could not reach backend at ${BACKEND_URL}`;
  }
  res.render('form', { items, error });
});

app.post('/add', async (req, res) => {
  try {
    await axios.post(`${BACKEND_URL}/api/items`, { name: req.body.name });
  } catch (err) {
    console.error('Error adding item:', err.message);
  }
  res.redirect('/');
});

app.get('/health', (req, res) => res.json({ status: 'ok' }));

app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
  console.log(`Using backend: ${BACKEND_URL}`);
});