from application import application


def test_home_returns_expected_message():
    client = application.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Hello from AWS CI/CD!"
    assert response.json["status"] == "running"


def test_health_endpoint():
    client = application.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
