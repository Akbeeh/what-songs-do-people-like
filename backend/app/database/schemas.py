from datetime import date
from typing import Optional

from pydantic import BaseModel


class SongCreate(BaseModel):
    song_id: str
    title: str
    artist: str
    image: str
    album: str
    release_date: date
    duration: str


class SongUpdate(BaseModel):
    song_id: Optional[str]
    title: Optional[str]
    artist: Optional[str]
    image: Optional[str]
    album: Optional[str]
    release_date: Optional[date]
    duration: Optional[str]
