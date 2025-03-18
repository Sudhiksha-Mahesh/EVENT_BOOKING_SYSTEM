from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_event():
    response = client.post(
        "/events/", json={"name": "Tech Conference", "date": "2025-06-01T10:00:00", "location": "New York"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Tech Conference"

def test_create_event_missing_field():
    response = client.post(
        "/events/", json={"name": "Incomplete Event"}
    )
    assert response.status_code == 422  # Expecting validation error

