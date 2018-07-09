from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

app = Flask(__name__)
application = app
app.config.from_object('config.base')

CORS(app)

auth = HTTPBasicAuth()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.mod_features.controllers import mod_features as features_module
app.register_blueprint(features_module)

@auth.get_password
def get_password(username):
    if username == 'iws':
        return 'pass'
    return None

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)