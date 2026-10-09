# Assignment 5 — Docker (Node.js + Flask)

A two-service web application: a **Node.js + Express frontend** serving an HTML form, and a **Flask backend** that receives the form submission and returns JSON. Both services are containerized separately with Docker and connected via **Docker Compose** on a shared bridge network.

**GitHub:** https://github.com/Umair-bey/tutedude-assignments/tree/main/Assignment-5

**Docker Hub Images:**
- Frontend → https://hub.docker.com/r/umairkhan2026/node-frontend
- Backend → https://hub.docker.com/r/umairkhan2026/flask-backend

---

## Tasks

### Task 1: Node.js Frontend
- Express server on port 3000
- Renders an HTML form (Name, Email, Message) via EJS
- On submit, forwards the POST data to the Flask backend
- Communicates with the backend using the Docker service name `backend` as the hostname

### Task 2: Flask Backend
- Exposes `GET /` (health check) and `POST /submit` endpoints
- Returns JSON with the received form data
- Uses `flask-cors` to allow cross-origin requests

### Task 3: Docker Configuration
- Separate `Dockerfile` for frontend (Node 18-alpine) and backend (Python 3.11-slim)
- `docker-compose.yml` wires both services on a shared bridge network (`app-network`)
- Frontend receives `BACKEND_URL=http://backend:5000` as an environment variable
- `backend` container depends on frontend startup order

### Task 4: Publishing
- Both images built, tagged, and pushed to Docker Hub
- Whole project pushed to GitHub
- `.gitignore` excludes `node_modules/`, `__pycache__/`, `.vscode/`, `.env`

---

## Project Structure

    Assignment-5/
    ├── frontend/
    │   ├── views/
    │   │   └── form.ejs         # HTML form template
    │   ├── app.js               # Express server
    │   ├── package.json         # Node dependencies
    │   └── Dockerfile           # Node image
    ├── backend/
    │   ├── app.py               # Flask app
    │   ├── requirements.txt     # Python dependencies
    │   └── Dockerfile           # Python image
    ├── docker-compose.yml       # Service orchestration
    ├── .gitignore
    ├── documentation.docx       # Full write-up (Word)
    └── documentation.pdf        # Full write-up (PDF)

---

## Routes

| Route | Method | Service | Purpose |
|-------|--------|---------|---------|
| `/` | GET | Frontend (3000) | Renders the HTML form |
| `/submit` | POST | Frontend (3000) | Forwards form data to Flask |
| `/` | GET | Backend (5000) | Health check — returns JSON |
| `/submit` | POST | Backend (5000) | Receives form data, returns JSON |

---

## Tech Stack

- **Frontend:** Node.js 18, Express 4.18, EJS, Axios, body-parser
- **Backend:** Python 3.11, Flask 3.0, flask-cors 4.0
- **Containerization:** Docker, Docker Compose
- **Registry:** Docker Hub
- **Orchestration:** Docker Compose (bridge network)

---

## Architecture

    ┌────────────────────┐         ┌────────────────────┐
    │  Node.js Frontend  │  HTTP   │   Flask Backend    │
    │  Container         │ ──────► │   Container        │
    │  Port 3000         │         │   Port 5000        │
    └────────┬───────────┘         └──────────┬─────────┘
             │                                │
             └──────── app-network ───────────┘
                    (Docker bridge)

The frontend reaches the backend via Docker's internal DNS — the service
name `backend` resolves automatically to the backend container's IP.

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Umair-bey/tutedude-assignments.git
cd tutedude-assignments/Assignment-5
```

### 2. Build and run with Docker Compose

```bash
docker compose up --build
```

### 3. Access the app

- **Frontend:** http://localhost:3000
- **Backend (direct):** http://localhost:5000

Fill in the form → click Submit → the JSON response from the Flask backend appears below the form.

### 4. Stop the containers

```bash
docker compose down
```

---

## Docker Hub

Pull the images directly:

```bash
docker pull umairkhan2026/node-frontend:latest
docker pull umairkhan2026/flask-backend:latest
```

Or run them:

```bash
docker run -p 3000:3000 umairkhan2026/node-frontend:latest
docker run -p 5000:5000 umairkhan2026/flask-backend:latest
```

---

## How It Works

1. User opens `http://localhost:3000` → Express serves the form
2. User fills the form and clicks Submit
3. Express (running in the frontend container) sends a POST request to `http://backend:5000/submit`
4. Docker's internal DNS resolves `backend` → backend container's IP
5. Flask processes the request and returns JSON
6. Express renders the success box with the JSON response

---

## Key Learnings

- Writing custom Dockerfiles for Node.js and Python applications
- Multi-container orchestration with `docker-compose.yml`
- Container-to-container communication over a user-defined bridge network
- Docker's internal DNS resolution using service names as hostnames
- Using environment variables to configure the backend URL dynamically
- Publishing images to Docker Hub and maintaining clean repos with `.gitignore`
