import requests

class BookingsAPI:
    BASE_URL = "http://localhost:8000/bookings"

    @staticmethod
    def create_booking(booking_data):
        response = requests.post(f"{BookingsAPI.BASE_URL}", json=booking_data)
        return response.json()

    @staticmethod
    def get_booking(booking_id):
        response = requests.get(f"{BookingsAPI.BASE_URL}/{booking_id}")
        return response.json()