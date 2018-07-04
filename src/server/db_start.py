import os

from flask import Flask, jsonify, request, make_response, url_for, current_app

from flask_restful import Resource, Api
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
# from flask_script import Manager

from config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "feature_request.db"))

db_connect = create_engine(database_file)

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db = SQLAlchemy(app)

# Is migrate necessary here
# # Change the migrations folder to be under models:
# MIGRATION_DIR = os.path.join('models', 'migrations')
# migrate = Migrate(app, db, directory=MIGRATION_DIR)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# migrate = Migrate(app, db)

conn = db_connect.connect()

auth = HTTPBasicAuth()

import controllers.feature_controller
# @app.errorhandler(400)
# def bad_request(error):
# 	print '404!!!!'
# 	return make_response(jsonify( { 'error': 'Bad request' } ), 400)

# @app.errorhandler(404)
# def not_found(error):
# 	print '400!!!!!'
# 	return make_response(jsonify( { 'error': 'Not found' } ), 404)


# @app.route('/api/features', methods = ['GET'])
# def query_all():
# 	# TODO: Come back and redo this the right way.
# 	conn = db_connect.connect()
# 	query = conn.execute("select * from feature")
# 	all_features = []
# 	for c in query:
# 		# titles.append([{"title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area}])
# 		all_features.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "product_area": c.product_area})
# 	all_features = {"features": all_features}
# 	resp = make_response(jsonify(all_features))
# 	resp.headers['Access-Control-Allow-Origin'] = '*'
# 	return resp



# app.route('/api/features', methods = ['GET'])(query_all())
# # app.errorhandler(400)(make_response(jsonify( { 'error': 'Bad request' } ), 400))
# app.errorhandler(404)(not_found(jsonify( { 'error': 'Not Found' } ), 404))
# app.route('/api/features', methods = ['GET'])(query_all(query = conn.execute("select * from feature")))




