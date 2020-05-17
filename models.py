from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
from constants import searchable_fields

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

db = SQLAlchemy()


class BaseModel(object):
    __searchable__ =  searchable_fields
    """
    Base Class to help handle DB repititive operations
    """
    
    def save(self):
        """
        Method for saving new data resource to the database
        """
        try:
            error = False
            db.session.add(self)
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        """
        Method for using sqlalchemy session ethods to delete
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()


class Venue(db.Model, BaseModel):
    """
    Model class for venue objects
    """
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    genres = db.Column(db.PickleType) # holds python objects serialised using a pickle. A list of genres. 
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seek_description = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    past_shows = db.Column(db.PickleType)
    upcoming_shows = db.Column(db.PickleType)
    past_shows_count = db.Column(db.Integer, default=0)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    venue_shows = db.relationship('Show', backref='Venue', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f"<Venue object: {self.name}>"


class Artist(db.Model, BaseModel):
    """
    Model class for Artists
    """
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    genres = db.Column(db.PickleType) # List containing genres serialized by a pickle
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seek_description = db.Column(db.String(300))
    image_link = db.Column(db.String(500))
    past_shows = db.Column(db.PickleType) 
    upcoming_shows = db.Column(db.PickleType)
    past_shows_count = db.Column(db.Integer, default=0)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    artist_shows = db.relationship('Show', backref='Artist', lazy=True, cascade='all, delete')
    
    def __repr__(self):
        return f"<Artist object: {self.name}>"


class Show(db.Model, BaseModel):
    """
    Model class for Shows
    """
    __tablename__ = 'Show'
    __searchable__ = []
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='CASCADE'),
                          nullable=False)
    artist_image_link = db.Column(db.String(300))
    artist_name = db.Column(db.String(120))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='CASCADE'),
                         nullable=False)
    venue_name = db.Column(db.String(120))
    date = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.String(120), nullable=False)
    end_time = db.Column(db.String(120), nullable=False)
    show_fee = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f"<Show object: {self.name}>"
