import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .credentials import auth
from .database.database import connect_to_database
from .database.models import Song
from .routers import songs, users
from .scheduler import scheduler_update_db

# With the help of https://fastapi.tiangolo.com/tutorial/bigger-applications/

# app = FastAPI(dependencies=[Depends(get_query_token), Depends(get_db)])
app = FastAPI(
    title="What songs do people like ?",
    contact={
        "name": "William M",
        "url": "https://github.com/Akbeeh",
    },
)

origins = [
    "http://localhost:5173",
    "localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(songs.router)


# NOTE: TOKEN IS ONLY AVAILABLE FOR ONE HOUR
@app.on_event("startup")
async def startup_event_get_token():
    # Generate the access token
    # auth.generate_access_token()

    # Generate the acces token + update the database
    await scheduler_update_db()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.get("/songs/{song_id}")
def get_song(song_id: str, db: Session = Depends(connect_to_database)):
    # Retrieve the song from the database using SQLAlchemy
    song = db.query(Song).filter(Song.song_id == song_id).first()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
