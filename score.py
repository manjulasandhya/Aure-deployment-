"""HTTP inference service for the Iris classification model."""

from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, request

MODEL_PATH = Path(__file__).with_name("model.pkl")
FEATURE_COUNT = 4

app = Flask(__name__)
model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    """Kubernetes health probe endpoint."""
    return jsonify(status="ok")


@app.post("/predict")
def predict():
    """Classify one Iris flower from four numeric measurements."""
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or "features" not in body:
        return jsonify(error="Send JSON with a 'features' array."), 400
    try:
        features = np.asarray(body["features"], dtype=float)
        if features.shape != (FEATURE_COUNT,):
            raise ValueError("'features' must contain exactly four numeric values.")
        prediction = int(model.predict(features.reshape(1, -1))[0])
        probabilities = model.predict_proba(features.reshape(1, -1))[0]
    except (TypeError, ValueError) as error:
        return jsonify(error=str(error)), 400
    return jsonify(prediction=prediction, probabilities=probabilities.tolist())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
