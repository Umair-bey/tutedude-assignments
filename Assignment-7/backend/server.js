const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/api', (req, res) => {
  res.json({ message: "Hello from Express Backend on Kubernetes!", status: "success" });
});

app.get('/api/health', (req, res) => {
  res.json({ status: "healthy" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
