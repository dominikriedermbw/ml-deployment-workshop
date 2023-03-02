import os.path

import onnxruntime as rt

path = os.path.dirname(os.path.abspath(__file__))

iris_classifier_session = rt.InferenceSession(f"{path}/persisted_models/trained_iris_model.onnx")

def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width) -> str:
    to_predict = [
        [sepal_length, sepal_width, petal_length, petal_width],
    ]

    result = iris_classifier_session.run(None, {'input': to_predict})
    return result[0].tolist()
