from secrets import refresh_token, base_64
import requests
import json

class Refresh:

    def __init__(self):
        super().__init__()
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):

        query = "https://acounts.spotify.com/api/token"
        reponse = requests.post()