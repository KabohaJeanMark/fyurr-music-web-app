Fyyur
-----

### Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

### Overview

This app is nearly complete. It is only missing one thing… real data! While the views and controllers are defined in this application, it is missing models and model interactions to be able to store retrieve, and update data from a database. By the end of this project, you should have a fully functioning site that is at least capable of doing the following, if not more, using a PostgreSQL database:

* creating new venues, artists, and creating new shows.
* searching for venues and artists.
* learning more about a specific artist or venue.

We want Fyyur to be the next new platform that artists and musical venues can use to find each other, and discover new music shows. Let's make that happen!

### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py *** Your forms
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css 
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      ├── forms
      ├── layouts
      └── pages
  ```

Overall:
* Models are located in the `models.py`
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`


Highlight folders:
* `templates/pages` -- (Already complete.) Defines the pages that are rendered to the site. These templates render views based on data passed into the template’s view, in the controllers defined in `app.py`. These pages successfully represent the data to the user, and are already defined for you.
* `templates/layouts` -- (Already complete.) Defines the layout that a page can be contained in to define footer and header code for a given page.
* `templates/forms` -- (Already complete.) Defines the forms used to create new artists, shows, and venues.
* `app.py` -- (Missing functionality.) Defines routes that match the user’s URL, and controllers which handle data and renders views to the user. This is the main file you will be working on to connect to and manipulate the database and render views with data to the user, based on the URL.
* Models in `app.py` -- (Missing functionality.) Defines the data models that set up the database tables.
* `config.py` -- (Missing functionality.) Stores configuration variables and instructions, separate from the main application code. This is where you will need to connect to the database.


Instructions
-----

1. Understand the Project Structure (explained above) and where important files are located.
2. Build and run local development following the Development Setup steps below.


### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)
