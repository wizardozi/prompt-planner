# backend/server.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from storage import DATA_FILE

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask!")

@app.route('/api/projects', methods=['GET'])
def get_projects():
    with open(DATA_FILE) as f:
        data = json.load(f)
    return jsonify(data['projects'])



if __name__ == '__main__':
    # app.run(debug=True, port=5000)
    app.run(host="127.0.0.1", port=5000, debug=True)