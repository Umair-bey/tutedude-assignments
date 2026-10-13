# Tutedude Assignments

This repository contains my assignments and practical work completed during the Tutedude course.

---

## 📚 Assignments

| Assignment | Topic | Status |
|---|---|---|
| [Assignment 1](./Assignment-1/) | Linux Basics | ✅ Completed |
| [Assignment 2](./Assignment-2/) | Python Basics | ✅ Completed |
| [Assignment 3](./Assignment-3/) | Flask & MongoDB (REST APIs) | ✅ Completed |
| [Assignment 4](./Assignment-4/) | Git & GitHub | ✅ Completed |
| [Assignment 5](./Assignment-5/) | Docker (Node.js + Flask) | ✅ Completed |
| [Assignment 6](./Assignment-6/) | AWS Deployment (EC2 + ECR + ECS) | ✅ Completed |
| [Assignment 7](./Assignment-7/) | Kubernetes Deployment (Minikube) | ✅ Completed |

---

## 📂 Repository Structure

```text
tutedude-assignments/
│
├── README.md
├── .gitignore
│
├── Assignment-1/
│   ├── README.md
│   └── screenshots/
│
├── Assignment-2/
│   ├── Assignment 2.docx
│   ├── assignment1.py
│   ├── student.txt
│   └── README.md
│
├── Assignment-3/
│   ├── README.md
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── .gitignore
│   ├── Documentation.docx
│   ├── Documentation.pdf
│   ├── data/
│   ├── templates/
│   └── screenshots/
│
├── Assignment-4/
│   ├── README.md
│   ├── app.py
│   ├── requirements.txt
│   ├── .gitignore
│   ├── UmairKhan_Assignment4_GitGitHub.pdf
│   ├── UmairKhan_Assignment4_GitGitHub.docx
│   ├── data/
│   ├── templates/
│   ├── static/
│   └── screenshots/
│
├── Assignment-5/
│   ├── README.md
│   ├── docker-compose.yml
│   ├── .gitignore
│   ├── documentation.docx
│   ├── documentation.pdf
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── frontend/
│       ├── app.js
│       ├── package.json
│       ├── Dockerfile
│       └── views/
│           └── form.ejs
│
├── Assignment-6/
│   ├── README.md
│   ├── AWS_UmairKhan.docx
│   ├── AWS_UmairKhan.pdf
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── frontend/
│   │   ├── app.js
│   │   ├── package.json
│   │   ├── Dockerfile
│   │   └── views/
│   │       └── form.ejs
│   └── screenshots/
│
└── Assignment-7/
    ├── README.md
    ├── Kubernetes_UmairKhan.docx
    ├── Kubernetes_UmairKhan.docx.pdf
    ├── backend/
    │   ├── Dockerfile
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   ├── package.json
    │   └── server.js
    ├── frontend/
    │   ├── Dockerfile
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   ├── app.py
    │   ├── requirements.txt
    │   └── templates/
    │       └── index.html
    └── screenshots/
```

---

## 🐧 Assignment 1 — Linux Basics

The first assignment focuses on fundamental Linux command-line operations.

### Topics Covered
- Creating and renaming files and directories
- Viewing file contents
- Searching for patterns using grep
- Zipping and unzipping files
- Downloading files using wget
- Changing file permissions
- Working with environment variables

👉 [View Assignment 1 →](./Assignment-1/)

---

## 🐍 Assignment 2 — Python Basics

The second assignment focuses on fundamental Python programming concepts.

### Topics Covered
- Taking user input
- Conditional statements using if-elif-else
- Grade checking
- Dictionaries
- Adding and updating student grades
- Loops
- Writing to a text file
- Reading from a text file
- Basic Python file handling

👉 [View Assignment 2 →](./Assignment-2/)

---

## 🌐 Assignment 3 — Flask & MongoDB (REST APIs)

The third assignment focuses on building REST APIs using Flask and MongoDB Atlas.

### Topics Covered
- Flask application setup and routing
- JSON API endpoints
- HTML templates with Jinja2
- Form handling (POST requests)
- MongoDB Atlas cloud database integration
- Inserting and reading documents with PyMongo
- Environment variables for secure credentials
- Success/error handling with redirects
- Deployment on Render

### Task 1: JSON API Route
- `/api` returns a JSON list read from a backend file (`data/data.json`).

### Task 2: Frontend Form with MongoDB Atlas
- Form at `/` submits data to MongoDB Atlas
- **On success:** redirect to `/success` showing "Data submitted successfully"
- **On error:** display the error on the same page without redirect

**Live Demo:** [https://flask-mongodb-umair.onrender.com](https://flask-mongodb-umair.onrender.com)

👉 [View Assignment 3 →](./Assignment-3/)

---

## 🔀 Assignment 4 — Git & GitHub

The fourth assignment focuses on practising the complete Git workflow — SSH setup, branching, merging, conflict resolution, sequential commits, `git reset`, and `git rebase` — using a Flask project with MongoDB Atlas integration.

### Topics Covered
- SSH key generation and GitHub integration
- Branch creation and management
- Merging branches (fast-forward and 3-way merges)
- Merge conflict resolution
- Parallel feature development with multiple branches
- Sequential commits for incremental changes
- `git reset --soft` to roll back while keeping changes staged
- `git rebase` to maintain linear commit history
- Deployment on Render with MongoDB Atlas

### Task 1: Repository Setup & First Branch
- Generated SSH key and added to GitHub
- Created branch `Umair`, committed an author comment in `app.py`
- Merged branch into `main`

### Task 2: Update JSON & Resolve Conflicts
- Created branch `Umair_new`
- Updated `data/data.json` with new content
- Caused and resolved a merge conflict by accepting `_new` changes

### Task 3: Parallel Feature Development
- Created branches `master_1` and `master_2` from `main`
- Built To-Do frontend page in `master_1`
- Built `/submittodotitem` backend route with MongoDB Atlas in `master_2`
- Merged both branches into `main` (resolved conflict)

### Task 4: Sequential Commits, Reset & Rebase
- Added 3 fields sequentially (Item ID → Item UUID → Item Hash) as 3 separate commits
- Used `git reset --soft` to roll back to Item ID commit
- Re-committed and rebased `master_1` onto updated `main`

### Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Home form |
| `/api` | GET | Returns JSON from `data/data.json` |
| `/todo` | GET | To-Do form with 5 fields |
| `/submittodotitem` | POST | Stores To-Do items in MongoDB |

**Live Demo:** [https://git-assignment-4-umair.onrender.com](https://git-assignment-4-umair.onrender.com)

**Documentation:** [UmairKhan_Assignment4_GitGitHub.pdf](./Assignment-4/UmairKhan_Assignment4_GitGitHub.pdf)

👉 [View Assignment 4 →](./Assignment-4/)

---

## 🐳 Assignment 5 — Docker (Node.js + Flask)

The fifth assignment focuses on containerizing a two-service web application using Docker and Docker Compose.

### Topics Covered
- Writing custom Dockerfiles for Node.js and Python applications
- Multi-container orchestration with `docker-compose.yml`
- Container-to-container communication over a user-defined bridge network
- Docker's internal DNS resolution using service names as hostnames
- Environment variables for dynamic configuration
- Publishing images to Docker Hub
- Deploying separate services on Render without compose

### Architecture
- **Frontend:** Node.js + Express (port 3000) — serves the HTML form
- **Backend:** Flask (port 5000) — receives form data and returns JSON
- **Network:** Both services connected via a user-defined Docker bridge network (`app-network`)
- **Communication:** Frontend reaches backend using the Docker service name `backend` as hostname

### Docker Hub Images
- Frontend → [umairkhan2026/node-frontend](https://hub.docker.com/r/umairkhan2026/node-frontend)
- Backend → [umairkhan2026/flask-backend](https://hub.docker.com/r/umairkhan2026/flask-backend)

### Live Demo (Deployed on Render)

| Service | URL |
|---|---|
| Frontend | https://node-frontend-umair.onrender.com |
| Backend (health check) | https://flask-backend-umair.onrender.com |

> ⚠️ Free tier: services sleep after 15 min of inactivity. First request may take 30–60s to wake up.

### Run Locally

```bash
git clone https://github.com/Umair-bey/tutedude-assignments.git
cd tutedude-assignments/Assignment-5
docker compose up --build
```

Access: http://localhost:3000

**Documentation:** [documentation.docx](./Assignment-5/documentation.docx)

👉 [View Assignment 5 →](./Assignment-5/)

---

## ☁️ Assignment 6 — AWS Deployment

The sixth assignment focuses on deploying a full-stack application (Flask backend + Express frontend) on AWS across three deployment architectures.

### Topics Covered
- EC2 provisioning (Ubuntu 24.04, `t3.micro`, free tier)
- Security groups — inbound AND outbound rules
- SSH access from Windows + `.pem` key permissions
- Linux process management with `nohup`
- Cross-server communication over public IP
- Docker image build + push to **Amazon ECR**
- Custom **VPC** with 2 public subnets, Internet Gateway, route tables
- **ECS Fargate** cluster, task definitions, and services
- Cost awareness — stopping services when not in use

### Architecture Overview

| Task | Deployment Pattern | Live URL |
|---|---|---|
| Task 1 | Single EC2 (both apps) | http://65.2.142.82:3000 |
| Task 2 | Two EC2s (backend + frontend) | http://15.206.205.213:3000 |
| Task 3 | Docker + ECR + ECS Fargate + VPC | http://13.201.96.116:3000 |

> ⚠️ Instances/services stopped after verification to avoid charges. Restart to access.

### Key Details

- **Backend:** Flask, port 5000
- **Frontend:** Express, port 3000
- **ECR Repos:** `flask-backend`, `express-frontend`
- **VPC:** `tutede-vpc-vpc` (`10.0.0.0/16`, 2 public subnets)
- **ECS Cluster:** `tutede-cluster` (Fargate only)
- **Task Definitions:** `tutede-backend-task:1`, `tutede-frontend-task:2`
- **Services:** `tutede-backend-service`, `tutede-frontend-service`

**Documentation:** [AWS_UmairKhan.pdf](./Assignment-6/AWS_UmairKhan.pdf)

👉 [View Assignment 6 →](./Assignment-6/)

---

## ☸️ Assignment 7 — Kubernetes Deployment (Minikube)

The seventh assignment focuses on deploying a full-stack application (Flask frontend + Express backend) on a local **Kubernetes cluster** using **Minikube**.

### Topics Covered
- Containerizing a Node.js backend and a Python/Flask frontend with custom Dockerfiles
- Local Kubernetes cluster provisioning with Minikube (Docker driver)
- Building images **inside** Minikube's Docker daemon with `minikube image build`
- Kubernetes **Deployments** for replica management (2 replicas each)
- Kubernetes **Services** — `ClusterIP` (internal) and `NodePort` (external)
- Inter-pod communication via Kubernetes **DNS service discovery**
- Environment variable injection through Deployment manifests
- Kubernetes Dashboard for visual cluster monitoring
- Debugging malformed files at the byte level
- DevOps safety net: custom Git **pre-commit hook** to block corrupted commits

### Architecture

| Component | Technology | Port | Service Type | Replicas |
|---|---|---|---|---|
| Frontend | Flask (Python 3.10) | 5000 | NodePort | 2 |
| Backend | Express (Node.js 18) | 3000 | ClusterIP | 2 |

**Communication flow:**

```
Browser → frontend-service (NodePort:5000) → Flask Pod
                                              ↓
                            http://backend-service:3000
                                              ↓
                            backend-service (ClusterIP) → Express Pod
```

Kubernetes internal DNS resolves `backend-service` to the correct pod IP — no hardcoded IPs.

### Key Commands

```powershell
# Start cluster
minikube start --driver=docker

# Build images inside Minikube
cd backend ; minikube image build -t backend:v1 . ; cd ..
cd frontend ; minikube image build -t frontend:v1 . ; cd ..

# Deploy
kubectl apply -f backend/deployment.yaml
kubectl apply -f backend/service.yaml
kubectl apply -f frontend/deployment.yaml
kubectl apply -f frontend/service.yaml

# Verify
kubectl get pods
kubectl get svc
kubectl get deployments
kubectl get all

# Access
minikube service frontend-service --url

# Dashboard
minikube dashboard
```

> ⚠️ On Windows, `minikube docker-env | Invoke-Expression` fails with an SSH agent error — use `minikube image build` instead.

> ⚠️ Keep the terminal running `minikube service frontend-service --url` open — Minikube's Docker driver on Windows holds the tunnel through it.

### Deployment Result

- **4 pods Running** (2 backend + 2 frontend), 0 restarts
- **2 Services** active — `backend-service` (ClusterIP), `frontend-service` (NodePort)
- **2 Deployments** at 2/2 replicas

**Documentation:** [Kubernetes_UmairKhan.docx](./Assignment-7/Kubernetes_UmairKhan.docx)

👉 [View Assignment 7 →](./Assignment-7/)

---

## 📊 Progress

**Assignments Completed:** 7  
**Total Assignments:** 7

```text
Assignment 1  ████████████████████  ✅
Assignment 2  ████████████████████  ✅
Assignment 3  ████████████████████  ✅
Assignment 4  ████████████████████  ✅
Assignment 5  ████████████████████  ✅
Assignment 6  ████████████████████  ✅
Assignment 7  ████████████████████  ✅
```

---

## 🛠️ Technologies & Tools

- Linux
- Bash
- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML / CSS
- Node.js
- Express
- Docker
- Docker Compose
- Docker Hub
- AWS (EC2, ECR, ECS Fargate, VPC)
- Kubernetes (Minikube)
- kubectl
- Render (deployment)
- Visual Studio Code
- Git
- GitHub

---

## 👨‍💻 Author

**Umair Khan**

DevOps Course — Tutedude
