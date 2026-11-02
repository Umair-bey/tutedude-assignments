from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/api')
@app.route('/api/')
def home():
    return "Hello from the Flask Backend running in ECS Fargate!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)