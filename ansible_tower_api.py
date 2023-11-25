import requests
from requests.auth import HTTPBasicAuth

class AnsibleTowerAPI:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{self.host}/api/v2/"

    def get_auth(self):
        return HTTPBasicAuth(self.username, self.password)

    def get_headers(self):
        return {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url, auth=self.get_auth(), headers=self.get_headers())
        return response.json()

    def post(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.post(url, auth=self.get_auth(), headers=self.get_headers(), json=data)
        return response.json()

    def put(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.put(url, auth=self.get_auth(), headers=self.get_headers(), json=data)
        return response.json()

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url, auth=self.get_auth(), headers=self.get_headers())
        return response.status_code