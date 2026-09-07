"""Train and persist a small, deterministic Iris classifier."""

from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

MODEL_PATH = Path(__file__).with_name("model.pkl")


def train() -> None:
    iris = load_iris()
    model = make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=500, random_state=42)
    )
    model.fit(iris.data, iris.target)
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    train()
