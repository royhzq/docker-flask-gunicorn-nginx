from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = {
        "status_code":200,
        "data":"Hello World"
    }
    return jsonify(response)