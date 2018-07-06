from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.base')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.mod_features.controllers import mod_features as features_module
app.register_blueprint(features_module)
