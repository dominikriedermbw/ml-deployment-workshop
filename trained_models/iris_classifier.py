import os.path

import numpy
from joblib import load
#import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
iris_classifier = load(f"{path}/persisted_models/trained_iris_model.joblib")

def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width) -> str:
    """to_predict = pd.DataFrame.from_dict(
        data={
            "sepal_length": [sepal_length],
            "sepal_width": [sepal_width],
            "petal_length": [petal_length],
            "petal_width": [petal_width]
        }
    )"""
    to_predict = [
        [sepal_length, sepal_width, petal_length, petal_width]
    ]

    result: numpy.ndarray = iris_classifier.predict(to_predict)
    return result.tolist()
