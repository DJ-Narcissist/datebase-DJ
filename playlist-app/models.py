"""Models for Playlist app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    artist_name = db.Column(db.String(100), nullable = False, unique = False)
    description = db.Column(db.String(500), nullable = False)
    #Relationship between Playlist and PlaylistSong
    songs = db.relationship('PlaylistSong', backref ='playlist', cascade = 'all, delete-orphan')
    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename = "songs"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    artist_name = db.Column(db.String(100), nullable = False)
    #Relationship between Song and PlaylistSong
    playlists = db.relationship('PlaylistSong', backref ='song', cascade ='all, delete-orphan')
    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlists_songs"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id', ondelete = 'CASCADE'), nullable = False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
