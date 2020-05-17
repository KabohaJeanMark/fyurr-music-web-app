#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from models import db, Artist, Show, Venue
from flask_whooshalchemyplus import index_all
import datetime
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  fetch_venues = db.session.query(Venue).group_by(Venue.id, Venue.state, Venue.city).all()
  if not fetch_venues:
    flash('There are no venues yet')
    return render_template('pages/venues.html')
  venue_array = []
  venue_keys = ['id', 'name', 'city', 'state']
  for venue in fetch_venues:
    venue_info = [venue.id, venue.name, venue.city, venue.state]
    venue_array.append(dict(zip(venue_keys, venue_info)))
  return render_template('pages/venues.html', venues=venue_array)

@app.route('/venues/search', methods=['POST'])
def search_venues():
  index_all(app)
  search_term = request.form.get('search_term','')
  result = Venue.query.whoosh_search(search_term).all()
  count = len(result)
  return render_template('pages/search_venues.html', results=result,search_term=request.form.get('search_term', ''),count=count)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  venue = Venue.query.filter_by(id=venue_id).first()
  data = venue.__dict__
  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submit():

  form = VenueForm(csrf_enabled=True)

  if form.validate_on_submit():
    venue_data = dict(
      name=form.name.data,
      genres=list(form.genres.data),
      address=form.address.data,
      city=form.city.data,
      state=form.state.data,
      phone=form.phone.data,
      website=form.website.data,
      facebook_link=form.facebook_link.data,
      seeking_talent=form.seeking_talent.data,
      seek_description=form.seek_description.data,
      image_link=form.image_link.data
      )
    venue_already_exists = Venue.query.filter_by(name=form.name.data).first()
    if venue_already_exists:
      flash('Error. There already exists a venue with that name. Please search for it or create another')
      return render_template('pages/home.html')
    brand_new_venue = Venue(** venue_data)
    brand_new_venue.save()

    flash('Venue ' + request.form['name'] + ' was successfully listed!')
    return render_template('pages/home.html')
  
  else:
    flash('An errror ocurred. Venue ' + request.form['name'] + ' could not be listed' )
    return render_template('pages/home.html')

  return render_template('pages/home.html')

#  Edit Venue
#  ----------------------------------------------------------------

@app.route('/venues/<venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue = Venue.query.filter_by(id=venue_id).first()
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  form = VenueForm(crsf_enabled=True)
  venue = Venue.query.filter_by(id=venue_id).first()
  try:
    if form.validate_on_submit():
      venue.name = form.name.data
      venue.city = form.city.data
      venue.state = form.state.data
      venue.address = form.address.data
      venue.phone = form.phone.data
      venue.genres = form.genres.data
      venue.seeking_talent = form.seeking_talent.data
      venue.seek_description = form.seek_description.data
      venue.image_link = form.image_link.data
      venue.website = form.website.data
      venue.facebook_link = form.facebook_link.data
      flash(f"{venue.name}'s data was successfully updated")
      db.session.commit()
      db.session.close()
  except:
    db.session.rollback()
    flash(f"{venue.name}'s data failed to be updated")
  finally:
    db.session.close()
    return redirect(url_for('show_venue', venue_id=venue_id))
  
  return render_template('pages/home.html')  

#  Delete Venue
#  ----------------------------------------------------------------
@app.route('/venues/<venue_id>/delete', methods=['POST'])
def delete_venue(venue_id):

  get_venue = Venue.query.filter_by(id=venue_id).first()
  if not get_venue:
    flash('The venue you want to delete does not exist. Please try another venue id')
  get_venue.delete()
  return render_template('pages/home.html')  

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  artists_list = Artist.query.all()
  return render_template('pages/artists.html', artists=artists_list)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  index_all(app)
  search_term=request.form.get('search_term', '')
  result = Artist.query.whoosh_search(search_term).all()
  count = len(result)
  return render_template('pages/search_artists.html', count=count, 
                         results=result, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  artist = Artist.query.filter_by(id=artist_id).first()
  data = artist.__dict__
  return render_template('pages/show_artist.html', artist=data)

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form = ArtistForm(csrf_enabled=True)
  if form.validate_on_submit():
    artist_data = dict(
      name=form.name.data,
      genres=list(form.genres.data),
      city=form.city.data,
      state=form.state.data,
      phone=form.phone.data,
      website=form.website.data,
      facebook_link=form.facebook_link.data,
      seeking_venue=form.seeking_venue.data,
      seek_description=form.seek_description.data,
      image_link=form.image_link.data
      )
    check_artist_exists = Artist.query.filter_by(name=form.name.data).first()
    if check_artist_exists:
      flash('Artist with that name already exists')
      return render_template('pages/home.html')
    new_artist = Artist(**artist_data)
    new_artist.save()
    flash('Artist ' + request.form['name'] + ' was successfully added!')
  else:
    errors = form.errors
    for key, error in errors.items():
      flash(f'{key}  Error ' + " => " + f"{error[0]} :(")
  return render_template('pages/home.html')

#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  today = datetime.date.today()
  today_shows = db.session.query(Show).filter(Show.date >= today).all()
  artist_data = []
  venue_data = []
  for show in today_shows:
    artist_info = Artist.query.filter_by(id=show.artist_id).first()
    venue_info = Venue.query.filter_by(id=show.venue_id).first()
    artist_data.append(artist_info)
    venue_data.append(venue_info)
  return render_template('pages/shows.html', shows=today_shows,
                         artists=artist_data, venues=venue_data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  form = ShowForm(csrf_enabled=True)
  artist = Artist.query.filter_by(id=form.artist_id.data).first()
  venue = Venue.query.filter_by(id=form.venue_id.data).first()
  if not artist:
    flash("The Artist does not exist yet. Please first create or choose another artist")
    return render_template('pages/home.html')
  elif artist.seeking_venue is False:
    flash("The Artists you selected is not seeking a venue")
    return render_template('pages/home.html')
  elif not venue:
    flash("The Venue selected does not exist yet. Please first create it or choose another venue")
    return render_template('pages/home.html')
  if form.validate_on_submit():
    show_data = dict(
      name=form.name.data,
      artist_id=form.artist_id.data,
      artist_image_link=artist.image_link,
      artist_name=artist.name,
      venue_id=form.venue_id.data,
      venue_name=venue.name,
      start_time=form.start_time.data,
      end_time=form.end_time.data,
      date=form.date.data,
      show_fee=form.fee.data
      )
    check_show_exists = Show.query.filter_by(name=form.name.data, venue_id=form.venue_id.data).first()
    if check_show_exists:
      flash('The Show you are trying to create already exists. Please create another one')
      return render_template('pages/home.html')
    new_show = Show(**show_data)
    new_show.save()
    flash('Show ' + request.form['name'] + ' was successfully added!')
  else:
    errors = form.errors
    for key, error in errors.items():
      flash(f'{key}  Error ' + " => " + f"{error[0]}")
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
