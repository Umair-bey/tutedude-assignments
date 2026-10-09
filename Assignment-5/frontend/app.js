const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const BACKEND_URL = process.env.BACKEND_URL || 'http://backend:5000';
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.render('form');
});

app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post(`${BACKEND_URL}/submit`, req.body);
    res.render('form', { result: response.data });
  } catch (err) {
    res.render('form', { error: err.message });
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend running on port ${PORT}`);
});