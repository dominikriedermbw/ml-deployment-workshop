import os.path

#from joblib import load
#import pandas as pd
#import pickle
import onnxruntime as rt
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
#iris_classifier = load(f"{path}/persisted_models/trained_iris_model.joblib")
#with open(f"{path}/persisted_models/trained_iris_model.pickle", "rb") as file:
#    iris_classifier = pickle.load(file)

sess = rt.InferenceSession(f"{path}/persisted_models/trained_iris_model.onnx")

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

    #result = iris_classifier.predict(to_predict)
    X = np.array([[sepal_length, sepal_width, petal_length, petal_width]], dtype=np.float32)
    result = sess.run(None, {'input': X})
    return result.tolist()
