# Imports necessary for bare bones flask app
#-----------------------

from config import Config
# Import flask
from flask import Flask
# import flask bootstrap
from flask_bootstrap import Bootstrap

#-----------------------

# Create the app variable
app = Flask(__name__)
app.config.from_object(Config)
# Define bootstrap, which takes app as a parameterself.
bootstrap = Bootstrap(app)

# import the routes file from app.
from app import routes
