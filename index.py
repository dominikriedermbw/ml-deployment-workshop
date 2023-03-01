# save this as index.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/more")
def hello_more():
    return "Hello, World! MORE"