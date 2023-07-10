from datetime import date
from typing import Optional

from pydantic import BaseModel


class SongCreate(BaseModel):
    title: str
    artist: str
    album: str
    release_date: date
    duration: int
    genre: str


class SongUpdate(BaseModel):
    title: Optional[str]
    artist: Optional[str]
    album: Optional[str]
    release_date: Optional[date]
    duration: Optional[int]
    genre: Optional[str]
