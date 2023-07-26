from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.database import (
    connect_to_database,
    get_songs_from_database,
    save_top_songs,
)
from ..database.repositories import SongRepository
from ..database.schemas import SongCreate, SongUpdate

# With the help of https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{song_id}")
def get_song(song_id: int, db: Session = Depends(connect_to_database)):
    # Use the SongRepository to retrieve the song by ID
    song = SongRepository(db).get_song(song_id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@router.get("/")
async def get_top_songs():
    # save_top_songs()
    songs = get_songs_from_database()

    # Return the top songs data
    return songs


@router.post("/")
def create_song(song_data: SongCreate, db: Session = Depends(connect_to_database)):
    # Use the SongRepository to create a new song
    song = SongRepository(db).create_song(song_data)
    return song


@router.put("/{song_id}")
def update_song(
    song_id: str, song_data: SongUpdate, db: Session = Depends(connect_to_database)
):
    # Use the SongRepository to update an existing song
    song = SongRepository(db).update_song(song_id, song_data)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@router.delete("/{song_id}")
def delete_song(song_id: str, db: Session = Depends(connect_to_database)):
    # Use the SongRepository to delete a song
    success = SongRepository(db).delete_song(song_id)
    if not success:
        raise HTTPException(status_code=404, detail="Song not found")
    return {"message": "Song deleted successfully"}
