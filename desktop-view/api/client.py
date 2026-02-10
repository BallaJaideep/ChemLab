# api/client.py

import requests
from app_state import AppState


class APIClient:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/"
        self.session = requests.Session()

    # ================= AUTH =================
    def login(self, username, password):
        url = self.base_url + "auth/login/"
        response = self.session.post(url, json={
            "username": username,
            "password": password
        })
        response.raise_for_status()
        return response.json()

    def register(self, username, email, password):
        url = self.base_url + "auth/register/"
        response = self.session.post(url, json={
            "username": username,
            "email": email,
            "password": password
        })
        response.raise_for_status()
        return response.json()

    # ================= AUTH HEADER =================
    def auth_headers(self):
        if AppState.token:
            return {
                "Authorization": f"Bearer {AppState.token}"
            }
        return {}
