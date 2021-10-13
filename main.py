import json
import requests
from secret import spotify_token, spotify_user_id, discover_weekly_id

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.discover_weekly_id = discover_weekly_id

    def find_songs(self):

        print("Finding songs in Discover Weekly Playlists")
        #loop through playlist tracks and add them to a list

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(discover_weekly_id)

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                "Authorization": "Bearer {}".format(spotify_token)})
        
        response_json = response.json()
        print(response_json)

        for i in response_json["items"]:
            print(i["track"]['name'])

a= SaveSongs()
a.find_songs()