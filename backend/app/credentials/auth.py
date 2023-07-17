import json
import os

from spotipy.oauth2 import SpotifyClientCredentials

CREDENTIALS_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "credentials.json"
)


def get_credentials():
    with open(CREDENTIALS_FILE) as file:
        credentials = json.load(file)
    return credentials


def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w+", encoding="utf-8") as file:
        json.dump(credentials, file, indent=2)


def generate_access_token():
    credentials = get_credentials()
    client_id = credentials["client_id"]
    client_secret = credentials["client_secret"]
    access_token = credentials["spotify_access_token"]

    # if not access_token:
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    access_token = client_credentials_manager.get_access_token(as_dict=False)
    credentials["spotify_access_token"] = access_token
    save_credentials(credentials)

    return access_token
