# from datetime import datetime
# from db_start import db
from server import db
import uuid


class Feature(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # id = db.Column(db.String(64), default=uuid.uuid4(), primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120))
    client = db.Column(db.String(64))
    # client_priority = db.Column(db.Integer())
    # target_date = db.Column(db.DateTime)
    product_area = db.Column(db.String(64))

    def __repr__(self):
        return '<Feature {}>'.format(self.title)

# def init_db():
#     db.create_all()

#     # # Create a test user
#     # new_user = User('a@a.com', 'aaaaaaaa')
#     # new_user.display_name = 'Nathan'
#     # db.session.add(new_user)
#     # db.session.commit()

#     # new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
#     # db.session.commit()


# if __name__ == '__main__':
#     init_db()