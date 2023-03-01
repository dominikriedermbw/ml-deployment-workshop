# save this as app.py
import os

from flask import Flask, Response, request

FLASK_API_KEY = os.getenv("FLASK_API_KEY")
app = Flask(__name__)


@app.before_request
def check_api_key():
    request_api_key = request.pa.get("api-key")
    if request_api_key != FLASK_API_KEY:
        return Response("Invalid Api Key", 401)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/more")
def hello_more():
    return "Hello, World! MORE"