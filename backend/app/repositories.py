from sqlalchemy.orm import Session

from .models import Song
from .schemas import SongCreate, SongUpdate


class SongRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_song(self, song_id: int) -> Song:
        return self.db.query(Song).get(song_id)

    def create_song(self, song_data: SongCreate) -> Song:
        song = Song(**song_data.dict())
        self.db.add(song)
        self.db.commit()
        self.db.refresh(song)
        return song

    def update_song(self, song_id: int, song_data: SongUpdate) -> Song:
        song = self.get_song(song_id)
        if song:
            for field, value in song_data.dict(exclude_unset=True).items():
                setattr(song, field, value)
            self.db.commit()
            self.db.refresh(song)
        return song

    def delete_song(self, song_id: int) -> bool:
        song = self.get_song(song_id)
        if song:
            self.db.delete(song)
            self.db.commit()
            return True
        return False
