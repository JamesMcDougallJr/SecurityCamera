import os
import flask
from flask_sslify import SSLify

app = flask.Flask(__name__)

if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)

db = SQLAlchemy(app)  # type: SQLAlchemy

from app.web import routes
