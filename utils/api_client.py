import requests

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers
        )