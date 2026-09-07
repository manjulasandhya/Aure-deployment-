import score


def test_health():
    response = score.app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_predict():
    response = score.app.test_client().post(
        "/predict", json={"features": [5.1, 3.5, 1.4, 0.2]}
    )
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["prediction"] in (0, 1, 2)
    assert len(payload["probabilities"]) == 3


def test_rejects_invalid_features():
    response = score.app.test_client().post("/predict", json={"features": [1, 2]})
    assert response.status_code == 400
