@'
# Assignment 7 - Kubernetes Deployment

Deploy a full-stack app (Flask frontend + Express backend) on Minikube.

## Stack
- Frontend: Flask (Python) on port 5000
- Backend: Express (Node.js) on port 3000
- Orchestration: Kubernetes (Minikube)

## Build Images
```bash
eval $(minikube docker-env)   # or: minikube docker-env | Invoke-Expression
docker build -t backend:v1 ./backend
docker build -t frontend:v1 ./frontend