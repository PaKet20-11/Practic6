import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

class Album(Base):
    __tablename__ = "album"
    id = sa.Column(sa.Integer, primary_key=True)
    year = sa.Column(sa.Integer)
    artist = sa.Column(sa.Text)
    genre = sa.Column(sa.Text)
    album = sa.Column(sa.Text)

new_album = {
    "artist" : "Queen",
    "genre" : "Rock",
    "album" : "Test Album Name",
    "year" : 2008
}

def add_album(album_dict):
    new_album = Album(
        artist= album_dict['artist'],
        genre=album_dict['genre'],
        album=album_dict['album'],
        year=album_dict['year']
    )
    session = connect_db()
    session.add(new_album)
    session.commit()

def all_albums(art):
    artists_alb = session.query(city).id()
    return artists_alb

add_album(new_album)