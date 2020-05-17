import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
from constants import genres_choices, state_choices


class ShowForm(Form):
    name = StringField(
        'name',
        validators=[DataRequired()]
    )
    artist_id = StringField(
        'artist_id',
        validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id',
        validators=[DataRequired()]
    )
    start_time = StringField(
        'start_time',
        validators=[DataRequired()]
    )
    end_time = StringField(
        'end_time',
        validators=[DataRequired()]
    )
    date = DateTimeField(
        'date',
        default=datetime.date.today()
    )
    fee = StringField(
        'fee',
        validators=[DataRequired()]
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
        'phone'
    )
    website = StringField(
        'website'
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    image_link = StringField(
        'image_link'
    )
    seeking_talent = BooleanField(
        'seeking_talent'
    )
    seek_description = StringField(
        'seek_description'
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
        'phone'
    )
    website = StringField(
        'website',
        validators=[URL()]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    seeking_venue = BooleanField(
        'seeking_venue'
    )
    seek_description = StringField(
        'seek_description'
    )
    image_link = StringField(
        'image_link'
    )

