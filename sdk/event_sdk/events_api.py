import requests

class EventsAPI:
    BASE_URL = "http://localhost:8000/events"

    @staticmethod
    def get_events():
        response = requests.get(f"{EventsAPI.BASE_URL}")
        return response.json()

    @staticmethod
    def get_event(event_id):
        response = requests.get(f"{EventsAPI.BASE_URL}/{event_id}")
        return response.json()
