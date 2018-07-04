# Import flask and template operators
from flask import Flask, render_template, Blueprint, make_response, jsonify

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from server.config import Config
from server.controllers.feature_controller import *

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object(Config)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404
# fapi = Blueprint('fapi', __name__, url_prefix='/api')

# from controllers.feature_controller import fapi as feature_api
print "registered"
# Register blueprint(s)
app.register_blueprint(fapi)
print "register achieve"
@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not found' } ), 404)

# Import a module / component using its blueprint handler variable (mod_auth)

# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()