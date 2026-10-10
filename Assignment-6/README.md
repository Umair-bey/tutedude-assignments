# AWS Deployment Assignment

Deploying a Flask backend + Express frontend on AWS using three configurations:

1. Single EC2 instance
2. Separate EC2 instances (backend & frontend)
3. Docker containers via ECR + ECS + VPC

## Project Structure
- backend/  → Flask API
- frontend/ → Express app (renders EJS, calls Flask API)

## Local Test
```bash
# Backend
cd backend && pip install -r requirements.txt && python app.py

# Frontend
cd frontend && npm install && BACKEND_URL=http://localhost:5000 node app.js