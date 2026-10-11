# Assignment 6 — AWS Deployment

**Name:** Umair Khan  
**Course:** DevOps | Tutedude  
**AWS Region:** ap-south-1 (Mumbai)

Deploying a **Flask backend** + **Express frontend** across three AWS architectures:

1. **Single EC2** — both apps on one server
2. **Separate EC2s** — backend and frontend on different servers
3. **Docker + ECR + ECS Fargate + custom VPC** — containerized microservices

---

## 📁 Project Structure

```
Assignment-6/
├── backend/                 # Flask REST API (port 5000)
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                # Express app (port 3000)
│   ├── app.js
│   ├── package.json
│   ├── views/form.ejs
│   └── Dockerfile
├── screenshots/             # Deployment evidence (all 3 tasks)
├── AWS_UmairKhan.docx       # Full documentation
├── AWS_UmairKhan.pdf        # PDF copy
└── README.md
```

**Backend (Flask)** — REST API endpoints:
- `GET  /api/items`  → list items
- `POST /api/items`  → add an item
- `GET  /health`     → health check

**Frontend (Express)** — renders a form that fetches data from the backend via the `BACKEND_URL` environment variable.

---

## 🧪 Local Test

**Terminal 1 — Backend:**
```bash
cd backend
pip install -r requirements.txt
python app.py              # http://localhost:5000
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm install
BACKEND_URL=http://localhost:5000 node app.js   # http://localhost:3000
```

Open `http://localhost:3000` → form + items from backend.

---

## ☁️ Task 1 — Single EC2 Instance

Flask + Express deployed together on one Ubuntu 24.04 EC2 (`t3.micro`).

| Field | Value |
|---|---|
| Instance ID | `i-0fd33e246d93e23c4` |
| Security Group | `tutede-aws-sg` (ports 22, 3000, 5000) |
| **Live URL** | **http://65.2.142.82:3000** |

- Used `nohup` to keep both processes running after SSH disconnect
- Instance stopped after verification (per assignment cost guidance)

---

## ☁️ Task 2 — Separate EC2 Instances

Flask on one EC2, Express on another — communicating over the public internet.

| Service | Public IP | Live URL |
|---|---|---|
| Backend (Flask) | `13.203.228.83` | http://13.203.228.83:5000 |
| Frontend (Express) | `15.206.205.213` | **http://15.206.205.213:3000** |

Frontend deployed with:
```bash
BACKEND_URL=http://13.203.228.83:5000 node app.js
```

**Troubleshooting:** The frontend security group's outbound rules were restricted to SSH-only, which blocked `apt update` and `npm install`. Fixed by changing outbound rules to **All traffic / 0.0.0.0/0**.

---

## ☁️ Task 3 — Docker + ECR + ECS Fargate + Custom VPC

Both apps containerized and deployed as ECS Fargate services inside a custom VPC.

### Docker Images → ECR

| Image | ECR Repository | Size |
|---|---|---|
| `flask-backend:latest` | `117647030291.dkr.ecr.ap-south-1.amazonaws.com/flask-backend` | 54.9 MB |
| `express-frontend:latest` | `117647030291.dkr.ecr.ap-south-1.amazonaws.com/express-frontend` | 73.2 MB |

### Custom VPC

| Resource | Value |
|---|---|
| VPC | `tutede-vpc-vpc` (`vpc-0f327aa819d1654a1`) |
| CIDR | `10.0.0.0/16` |
| Public Subnets | 2 (ap-south-1a, ap-south-1b) |
| Internet Gateway | `tutede-vpc-igw` |
| Route Table | `tutede-vpc-rtb-public` (0.0.0.0/0 → IGW) |

### ECS Setup

- **Cluster:** `tutede-cluster` (Fargate only)
- **Task Definitions:**
  - `tutede-backend-task:1` — flask-backend, port 5000
  - `tutede-frontend-task:2` — express-frontend, port 3000, `BACKEND_URL=http://43.204.231.169:5000`
- **Services:**
  - `tutede-backend-service` — 1 task
  - `tutede-frontend-service` — 1 task

### Live URLs

| Service | ECS Task Public IP | Live URL |
|---|---|---|
| Backend (Flask) | `43.204.231.169` | http://43.204.231.169:5000 |
| Frontend (Express) | `13.201.96.116` | **http://13.201.96.116:3000** |

Both services scaled to **Desired tasks = 0** after verification to avoid ongoing charges.

---

## 📸 Screenshots

All deployment evidence is in the [`screenshots/`](./screenshots) folder:

- **Setup** — AWS account creation, verification, health check
- **Task 1** — EC2 launch, SSH session, both processes running, live browser
- **Task 2** — Two EC2 instances, cross-server communication, browser test
- **Task 3** — Docker images, VPC creation, ECS cluster, task definitions, services, live browser

---

## 📄 Full Documentation

See [`AWS_UmairKhan.docx`](./AWS_UmairKhan.docx) (or [`.pdf`](./AWS_UmairKhan.pdf)) for the complete write-up including:

- Detailed deployment commands for all 3 tasks
- All screenshots with captions
- Configuration tables (EC2, VPC, ECS, security groups)
- Troubleshooting notes

---

## 🧠 Key Learnings

1. **EC2 provisioning** — launching, securing, connecting to virtual servers
2. **Security Groups** — inbound AND outbound rules matter; misconfigured egress blocks package installation
3. **Process management** — `nohup` keeps apps running after SSH disconnect
4. **Cross-server communication** — frontend EC2 → backend EC2 via public IP
5. **Docker** — building minimal, layer-cached images
6. **ECR** — private Docker registry with token-based auth
7. **VPC** — custom networking with public subnets, IGW, route tables
8. **ECS Fargate** — serverless container orchestration
9. **Cost awareness** — stopping instances/services when not in use

---

## 🔗 Links

- **GitHub Repository:** https://github.com/Umair-bey/tutedude-assignments
- **Live App (Task 1):** http://65.2.142.82:3000 *(EC2 stopped — restart to access)*
- **Live App (Task 2):** http://15.206.205.213:3000 *(EC2 stopped — restart to access)*
- **Live App (Task 3):** http://13.201.96.116:3000 *(ECS tasks stopped — scale to 1 to access)*