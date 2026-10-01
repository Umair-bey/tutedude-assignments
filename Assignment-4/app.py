# Task 1: Umair's branch - Git Assignment 4
import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# ============================================================
# TASK 1: JSON API Route — reads data from a backend file
# ============================================================
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'data.json')

def read_data_file():
    """Read the JSON list from the backend file."""
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

@app.route('/api', methods=['GET'])
def api():
    """Return the JSON list stored in data.json"""
    data = read_data_file()
    return jsonify(data)


# ============================================================
# TASK 2: Frontend Form → MongoDB Atlas
# ============================================================
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database('tutedude_db')
collection = db['submissions']


@app.route('/')
def index():
    """Show the form."""
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission."""
    try:
        data = request.form.to_dict()
        if not data.get('name') or not data.get('email'):
            raise ValueError("Name and Email are required.")
        collection.insert_one(data)
        # Success: redirect to a different page
        return redirect(url_for('success'))
    except Exception as e:
        # Error: render the same page with the error message
        return render_template('index.html', error=str(e))


@app.route('/success')
def success():
    """Success page shown after form submission."""
    return render_template('success.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')
@app.route('/submittodotitem', methods=['POST'])
def submit_todo_item():
    """Handle To-Do form submission and store in MongoDB."""
    try:
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')

        if not item_name or not item_description:
            raise ValueError("Item Name and Item Description are required.")

        collection.insert_one({
            'itemName': item_name,
            'itemDescription': item_description
        })

        return redirect(url_for('todo'))
    except Exception as e:
        return render_template('todo.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)