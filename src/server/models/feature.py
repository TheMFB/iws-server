from datetime import datetime
from app import db
import uuid


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # id = db.Column(uuid.uuid4(), primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120))
    client = db.Column(db.String(64))
    # client_priority = db.Column(db.Integer())
    # target_date = db.Column(db.DateTime)
    product_area = db.Column(db.String(64))

    def __repr__(self):
        return '<Feature {}>'.format(self.title)