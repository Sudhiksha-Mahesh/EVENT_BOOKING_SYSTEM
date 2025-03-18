from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_booking():
    response = client.post(
        "/bookings/", json={"user_id": 1, "event_id": 1}
    )
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_booking_invalid_user():
    response = client.post(
        "/bookings/", json={"user_id": 999, "event_id": 1}
    )
    assert response.status_code == 400  # Expecting invalid user error
