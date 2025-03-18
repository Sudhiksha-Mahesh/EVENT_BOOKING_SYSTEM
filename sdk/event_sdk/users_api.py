import requests

class UsersAPI:
    BASE_URL = "http://localhost:8000/users"

    @staticmethod
    def register_user(user_data):
        response = requests.post(f"{UsersAPI.BASE_URL}/register", json=user_data)
        return response.json()

    @staticmethod
    def login(credentials):
        response = requests.post(f"{UsersAPI.BASE_URL}/login", json=credentials)
        return response.json()