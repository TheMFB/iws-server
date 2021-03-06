from app import db, migrate

from sqlalchemy import update
from sqlalchemy_utils.types import UUIDType

import datetime
import uuid

class Feature(db.Model):
    __tablename__ = "features"
    id = db.Column(UUIDType(), default=uuid.uuid4, primary_key=True)
    title = db.Column(db.String(64), default='No Title', index=True)
    description = db.Column(db.String(120), default='No Description')
    client = db.Column(db.String(64), default='No Client')
    client_priority = db.Column(db.Integer(), default='0')
    target_date = db.Column(db.DateTime(), default='2000-01-01 00:00:00')
    product_area = db.Column(db.String(64), default='Policies')

    def __repr__(self):
        return '<Feature {}>'.format(self.title)

def get_all():
    feature_query = Feature.query.all()
    all_features = []
    for c in feature_query:
        all_features.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area})
    return all_features

def get_clients(client):
    client_query = Feature.query.filter(Feature.client == client)
    all_clients = []
    for c in client_query:
        all_clients.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area})
    print all_clients
    return all_clients

def get_client_list():
    client_list = []
    for value in db.session.query(Feature.client).distinct():
        client_list.append(value[0])
    return client_list

def add(f):
    db.session.add(f)
    db.session.commit()
    db.session.close()
    return 'Feature Created', 201

def update(id, content):
    Feature.query.filter_by(id=id).update(content)
    db.session.commit()
    db.session.close()
    return 'Updated feature', 201

def remove(id):
    Feature.query.filter_by(id=id).delete()
    db.session.commit()
    db.session.close()
    return 'Removed Feature', 201

def remove_all():
    features = Feature.query.all()
    for f in features:
        db.session.delete(f)
    db.session.commit()
    db.session.close()
    return 'Removed ALL features', 201

def change_priority(client_name, feature_priority): #feature priority =[feature_id1, feature_id2, ... feature_idn]
    features = Feature.query.filter_by(client=client_name)
    features_unknown_indx = features.count()
    for feature in features:
        indx = feature_priority.index(str(feature.id))
        if indx >= 0:
            feature.client_priority = indx + 1
        else:
            feature.client_priority = features_unknown_indx + 1  # This is a large integer to stick it at the end of the list.
            features_unknown_indx += 1


    db.session.commit()
    db.session.close()
    return 'Feature Created', 200

# I'll leave this here, just in case...
# def init_db():
#     db.create_all()

#     db.session.add(Feature(title="t1", description="d1", client="c1", client_priority="1", target_date=datetime.datetime(2018, 3, 24, 2, 9, 12), product_area="p1"))
#     db.session.commit()
#     db.session.close()

# init_db()