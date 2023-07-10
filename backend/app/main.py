import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .dependencies import get_db, get_query_token, get_token_header
from .models import Song
from .routers import songs, users

# With the help of https://fastapi.tiangolo.com/tutorial/bigger-applications/

# app = FastAPI(dependencies=[Depends(get_query_token), Depends(get_db)])
app = FastAPI(
    title="What songs do people like ?",
    contact={
        "name": "William M",
        "url": "https://github.com/Akbeeh",
    },
)


app.include_router(users.router)
app.include_router(songs.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.get("/songs/{song_id}")
def get_song(song_id: int, db: Session = Depends(get_db)):
    # Retrieve the song from the database using SQLAlchemy
    song = db.query(Song).filter(Song.song_id == song_id).first()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
