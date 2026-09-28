# Assignment 3 — Flask & MongoDB

A Flask application with a JSON API route and a frontend form that stores data in MongoDB Atlas.

## Task 1: JSON API Route
- `/api` returns a JSON list read from `data/data.json`

## Task 2: Frontend Form with MongoDB Atlas
- Form at `/` submits to `/submit`
- On success: redirects to `/success` showing "Data submitted successfully"
- On error: displays error on the same page without redirect

## Project Structure

    Assignment-3/
    ├── app.py                  # Main Flask application
    ├── requirements.txt        # Python dependencies
    ├── .gitignore              # Excludes .env, .venv, __pycache__
    ├── data/data.json          # Backend file for Task 1
    ├── templates/
    │   ├── index.html          # Form page
    │   └── success.html        # Success page
    ├── screenshots/            # Evidence screenshots
    ├── Documentation.docx      # Full write-up (Word)
    └── Documentation.pdf       # Full write-up (PDF)

## Tech Stack
- Python 3.14
- Flask 3.1.3
- PyMongo 4.18.1
- dnspython 2.8.0
- python-dotenv 1.2.3
- MongoDB Atlas (Free M0 tier)

## Setup & Run

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    python app.py

Open in browser:
- `http://127.0.0.1:5000/` — Form page (Task 2)
- `http://127.0.0.1:5000/api` — JSON API (Task 1)

## Author
**Umair Khan** — Tutedude DevOps Student
