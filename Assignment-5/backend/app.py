import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Flask Backend is running!"})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form if request.form else request.get_json()
    return jsonify({
        "status": "success",
        "received": {
            "name": data.get('name'),
            "email": data.get('email'),
            "message": data.get('message')
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)