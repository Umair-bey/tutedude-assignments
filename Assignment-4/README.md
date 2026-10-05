# Assignment 4: Git & GitHub

**Author:** Umair Khan  
**Course:** Tutedude DevOps  
**Repo:** https://github.com/Umair-bey/tutedude-assignments  

---

## 🌐 Live Demo

**Deployed URL:** https://git-assignment-4-umair.onrender.com

| Page | URL |
|------|-----|
| Home | https://git-assignment-4-umair.onrender.com/ |
| To-Do Form | https://git-assignment-4-umair.onrender.com/todo |
| API | https://git-assignment-4-umair.onrender.com/api |

**Hosted on:** Render.com (free tier)  
**Database:** MongoDB Atlas (Cluster0 → tutedude_db → submissions)

> ⚠️ **Note:** Since the app runs on Render's free tier, it sleeps after 
> 15 minutes of inactivity. The first request after sleeping may take 
> 30–60 seconds to load.

---

## Tasks Completed

- **Task 1:** Repository setup, SSH key generation, branch `Umair` created 
  and merged to `main`
- **Task 2:** Branch `Umair_new`, `data.json` update, merge conflict 
  resolved by accepting `_new` changes
- **Task 3:** Parallel branches `master_1` (frontend To-Do page) and 
  `master_2` (backend `/submittodotitem` API with MongoDB Atlas), merged 
  to `main`
- **Task 4:** Sequential commits (Item ID → Item UUID → Item Hash), 
  `git reset --soft`, and `git rebase` preserving commit history

---

## Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home form (legacy) |
| `/api` | GET | Returns JSON from `data/data.json` |
| `/todo` | GET | To-Do form with 5 fields |
| `/submittodotitem` | POST | Stores To-Do items in MongoDB |
| `/submit` | POST | Legacy form submission |
| `/success` | GET | Success page |

---

## Tech Stack

- **Backend:** Flask 3.1.3
- **Database:** MongoDB Atlas (via PyMongo 4.18.1)
- **Server:** Gunicorn 23.0.0
- **Env Management:** python-dotenv 1.0.1
- **Hosting:** Render.com

---

## Local Setup

### 1. Clone the repository

```bash
git clone git@github.com:Umair-bey/tutedude-assignments.git
cd tutedude-assignments/Assignment-4