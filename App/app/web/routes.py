import os
import flask
from importlib import import_module
from app import app

# import camera driver
#if os.environ.get('CAMERA'):
#    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
#    from ..backend.camera import Camera

from .. import py_camera

@app.route('/')
def index():
    """Video streaming home page."""
    return flask.render_template('root.html')


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
