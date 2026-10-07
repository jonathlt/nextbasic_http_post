from flask import Flask
from time import strftime
import time
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def hello_world():
    logging.info("Handling request for root path")
    return "<h1>Hello, World!</h1>"

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

@app.route("/api/highscore", methods=["POST"])
def update_highscore():
    logging.info("Handling POST request to update highscore")
    # Implementation for updating highscore
    return "Highscore updated successfully"