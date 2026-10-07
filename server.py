from flask import Flask
from time import strftime
from flask import request
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def hello_world():
    logging.info("Handling request for root path")
    return "<h1>Hello, World!</h1>"

@app.before_request
def log_request_info():
    logging.info("Received %s request for %s from %s", request.method, request.path, request.remote_addr)
    logging.info("Request headers: %s", request.headers)
    logging.info("Request body: %s", request.get_data())

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logging.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

@app.route("/api/highscore", methods=["POST"])
def update_highscore():
    logging.info("Handling POST request to update high score")
    # Implementation for updating high score
    return "High score updated successfully"