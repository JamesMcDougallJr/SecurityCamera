import os
import flask
from importlib import import_module
from app import app

from .. import py_camera

@app.route('/')
def index():
    """Video streaming home page."""
    if 'DYNO' in os.environ:
        return flask.render_template('root.html')
    return flask.render_template('root_pi.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return flask.Response(gen(py_camera.Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
