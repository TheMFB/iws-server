import os

from flask import Flask, request, make_response, url_for

from flask_restful import Resource, Api
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
# from flask_script import Manager

from config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from json import dumps
# from app.models import Feature
# from app import db
from controllers.feature import FeatureHelper


# from flask.ext.jsonpify import jsonify

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
migrate = Migrate(app, db)

conn = db_connect.connect()
auth = HTTPBasicAuth()



if __name__ == '__main__':
	# manager.run()
	app.run(port='5002')


