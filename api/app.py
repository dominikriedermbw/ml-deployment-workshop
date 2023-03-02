# save this as app.py
import os
from flask import Flask, Response
from flask import request as flask_request

import sys
sys.path.append("..")
from trained_models import iris_classifier

dir_path = os.path.dirname(os.path.abspath(__file__))

FLASK_API_KEY = os.getenv("FLASK_API_KEY")
app = Flask(__name__)


"""@app.before_request
def check_api_key():
    request_api_key = request.headers.get("api-key")
    if request_api_key != FLASK_API_KEY:
        return Response("Invalid Api Key", 401)"""

@app.route("/")
def api_info():
    return {
        "/predict_iris_species ": "params: sepal_length, sepal_width, petal_length, petal_width",
        "/": "endpoint infos"
    }

@app.route("/another")
def another():
    return {
        "/predict_iris_species ": "params: sepal_length, sepal_width, petal_length, petal_width",
        "/": "endpoint infos"
    }

@app.route("/predict_iris_species")
def predict_iris_species():
    try:
        #breakpoint()
        #return iris_classifier.predict_iris_species(**request.json)
        return flask_request.json
    except Exception as e:
        return f"An error occured: {str(e)}."
    """return iris_classifier.predict_iris_species(
        sepal_length=5.0,
        sepal_width=5.0,
        petal_length=5.0,
        petal_width=5.0
    )"""

if __name__ == "__main__":
    app.run(host="localhost", port=8000)