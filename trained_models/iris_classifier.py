import os.path
from typing import List

import numpy
from joblib import load
from sklearn.svm import SVC
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
iris_classifier: SVC = load(f"{path}/persisted_models/trained_iris_model.joblib")

def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width) -> str:
    to_predict = pd.DataFrame.from_dict(
        data={
            "sepal_length": [sepal_length],
            "sepal_width": [sepal_width],
            "petal_length": [petal_length],
            "petal_width": [petal_width]
        }
    )

    result: numpy.ndarray = iris_classifier.predict(to_predict)
    return result.tolist()

"""print(predict_iris_species(
    6.0, 2.0, 2.0, 0.4
))"""