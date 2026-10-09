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

---

## 📂 Repository Structure

```text
tutedude-assignments/
│
├── README.md
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
└── Assignment-5/
    ├── README.md
    ├── docker-compose.yml
    ├── .gitignore
    ├── documentation.docx
    ├── documentation.pdf
    ├── backend/
    │   ├── app.py
    │   ├── requirements.txt
    │   └── Dockerfile
    └── frontend/
        ├── app.js
        ├── package.json
        ├── Dockerfile
        └── views/
            └── form.ejs
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
|-------|--------|---------|
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
|---------|-----|
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

## 📊 Progress

**Assignments Completed:** 5  
**Total Assignments:** 5

```text
Assignment 1  ████████████████████  ✅
Assignment 2  ████████████████████  ✅
Assignment 3  ████████████████████  ✅
Assignment 4  ████████████████████  ✅
Assignment 5  ████████████████████  ✅
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
- Render (deployment)
- Visual Studio Code
- Git
- GitHub

---

## 👨‍💻 Author

**Umair Khan**

DevOps Course — Tutedude
```


Upload `Docker_UmairKhan.zip` to the Tutedude portal. 🚀