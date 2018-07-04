import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pawssword'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'feature_request.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

