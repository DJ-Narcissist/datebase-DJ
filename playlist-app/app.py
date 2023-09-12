from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    
    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK(PLAYLIST BY ID)
    playlist = Playlist.query.get_or_404(playlist_id)

    return render_template("playlist.html", playlist = playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()

    if form.validate_on_submit():
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        # New playlist based on form
        new_playlist = Playlist(
            artist_name = form.artist_name.data,
            description = form.description.data
        )

        db.session.add(new_playlist)
        db.session.commit()

    return render_template("new_playlist.html", form = form)

##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK(SOng by id)
    song = Song.query_get_or_404(song_id)

    return render_template("new_song.html",  song = song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    
    if form.validate_on_submit():
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # New song based off form
        new_song = Song(
            title = form.title.data,
            artist_name = form.artist_name.data
        )

        db.session.add(new_song)
        db.session.commit()

    return render_template('new_song.html')
@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = [entry.song_id for entry in playlist.songs]
    form.song.choices = [(song.id, song.title) for song in Song.query.filter(Song.id.nothin_(curr_on_playlist)).all()]

    if form.validate_on_submit():

          # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        song_id = form.song.data
        song = Song.query.get(song_id)
        if song : Song.query.get(song_id)
        playlist_song = PlaylistSong(playlist_id = playlist_id, song_id = song_id)
        db.session.add(playlist_song)
        db.session.commit()


        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
