"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    artist_name = StringField('Artist Name', validators = [DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators = [DataRequired()])
    artist_name = StringField('Artist Name', validators = [DataRequired()])
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
