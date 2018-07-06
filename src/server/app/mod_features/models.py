from app import db, migrate
import datetime
import uuid


class Feature(db.Model):
    __tablename__ = "features"
    id = db.Column(db.String(64), default=str(uuid.uuid4()), primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(120))
    client = db.Column(db.String(64))
    client_priority = db.Column(db.Integer())
    target_date = db.Column(db.DateTime())
    product_area = db.Column(db.String(64))

    def __repr__(self):
        return '<Feature {}>'.format(self.title)

def query_all():
    # feature_query = list(self.query.all())
    feature_query = Feature.query.all()
    all_features = []
    for c in feature_query:
        all_features.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "clien_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area})
    return all_features

def create_feature(f):
    try:
        db.session.add(f)
        db.session.commit()
        return 'true', 201
    except Exception as e:
        print e
        return 'An error was raised. This probably wasn\'t too helpful', 500


def init_db():
    print "init_db"

    # db.create_all()

    # db.session.add(Feature(title="t1", description="d1", client="c1", client_priority="1", target_date=datetime.datetime(2018, 3, 24, 2, 9, 12), product_area="p1"))
    # db.session.commit()
    # print Feature.query.all()
    # db.session.close()
    # print 'close'


init_db()