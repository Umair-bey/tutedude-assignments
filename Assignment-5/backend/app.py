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
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    return jsonify({
        "status": "success",
        "received": {
            "name": name,
            "email": email,
            "message": message
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
