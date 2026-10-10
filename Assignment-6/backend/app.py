from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend (different EC2 / container) to call this API

# In-memory store (fine for assignment)
items = []

@app.route('/')
def home():
    return jsonify({"message": "Flask Backend is running on AWS!"})

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "name is required"}), 400
    item = {"id": len(items) + 1, "name": data['name']}
    items.append(item)
    return jsonify(item), 201

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # host=0.0.0.0 is IMPORTANT for EC2 / Docker
    app.run(host='0.0.0.0', port=5000)