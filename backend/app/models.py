from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime)


class Song(Base):
    __tablename__ = "song"

    song_id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    artist = Column(String)
    album = Column(String)
    release_date = Column(Date)
    duration = Column(Integer, nullable=False)
    genre = Column(String)


class Rating(Base):
    __tablename__ = "rating"

    rating_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    song_id = Column(Integer, ForeignKey("song.song_id"))
    rating = Column(Integer)
    timestamp = Column(DateTime)

    user = relationship("User", backref="ratings")
    song = relationship("Song", backref="ratings")
