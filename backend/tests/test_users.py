from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/", json={"username": "testuser", "email": "test@example.com", "password": "securepass"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_create_user_duplicate():
    response = client.post(
        "/users/", json={"username": "testuser", "email": "test@example.com", "password": "securepass"}
    )
    assert response.status_code == 400  # Expecting duplicate user error

