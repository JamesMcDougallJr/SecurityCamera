import os
import flask
from flask_sslify import SSLify

app = flask.Flask(__name__)

if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)

from app.backend import py_camera
from app.web import routes