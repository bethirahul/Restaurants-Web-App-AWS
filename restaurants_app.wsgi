# WSGI file for the application, sets the application path
import sys
import os

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))

from flask_app import app as application