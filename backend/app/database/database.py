from datetime import date
from typing import List

import requests
from app.credentials.auth import get_credentials
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Song
from .repositories import SongRepository
from .schemas import SongCreate


def retrieve_data_from_spotify() -> dict:
    # Retrieve the access token from the credentials
    access_token = get_credentials()["spotify_access_token"]

    # id_global_playlist = "37i9dQZEVXbMDoHDwVN2tF"
    id_global_playlist = "3cEYpjA9oz9GiPac4AsH4n"

    # Make a request to the Spotify API
    response = requests.get(
        url=f"https://api.spotify.com/v1/playlists/{id_global_playlist}",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    # Process the response and extract the top songs data
    data = response.json()

    return data


# def retrieve_songs_from_data(data):
#     # Only retrieve id, title, artist, album, release_date, duration
#     data = data["tracks"]["items"]
#     ids = [item["track"]["id"] for item in data]
#     titles = [item["track"]["name"] for item in data]
#     artists = [artist["name"] for item in data for artist in item["track"]["artists"]]
#     albums = [item["track"]["album"]["name"] for item in data]
#     release_dates = [item["track"]["album"]["release_date"] for item in data]
#     duration = [
#         f"{divmod(item['track']['duration_ms'] // 1000, 60)[0]:02d}:{divmod(item['track']['duration_ms'] // 1000, 60)[1]:02d}"
#         for item in data
#     ]

# with open("./app/database/temp.json", "w+", encoding="utf-8") as file:
#     json.dump(data, file, indent=2)
# return ids, titles, artists, albums, release_dates, duration


def connect_to_database():
    # Function to establish connection with the PostgreSQL database
    db_url = "postgresql://wsdpl:wsdplPW@localhost:5432/wsdpldb"
    engine = create_engine(db_url)

    # Create a session factory
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create the table in the database (if it doesn't already exist)
    Base.metadata.create_all(bind=engine)

    return SessionLocal()


def retrieve_songs_from_data(data: List[dict]) -> List[SongCreate]:
    # Only retrieve id, title, artist, album, release_date, duration
    songs = []
    for item in data["tracks"]["items"]:
        song_data = SongCreate(
            song_id=item["track"]["id"],
            title=item["track"]["name"],
            artist=item["track"]["artists"][0]["name"],
            album=item["track"]["album"]["name"],
            release_date=date.fromisoformat(item["track"]["album"]["release_date"]),
            duration=f"{divmod(item['track']['duration_ms'] // 1000, 60)[0]:02d}:{divmod(item['track']['duration_ms'] // 1000, 60)[1]:02d}",
        )
        songs.append(song_data)
    return songs


def sync_top_songs(songs: List[SongCreate]):
    db = connect_to_database()
    song_repository = SongRepository(db)

    # Get the existing song ids from the database
    existing_song_ids = [song.song_id for song in song_repository.get_all_songs()]

    # Insert new songs and skip existing ones
    for song_data in songs:
        if song_data.song_id not in existing_song_ids:
            song_repository.create_song(song_data)

    # Delete songs that are no longer in the top songs
    for song_id in existing_song_ids:
        if song_id not in [song.song_id for song in songs]:
            song_repository.delete_song(song_id)


def save_top_songs():
    # Function to save songs to the database
    data = retrieve_data_from_spotify()
    songs = retrieve_songs_from_data(data)
    sync_top_songs(songs)


def get_songs_from_database() -> List[Song]:
    # Function to retrieve songs from the database
    db = connect_to_database()
    song_repository = SongRepository(db)
    return song_repository.get_all_songs()
