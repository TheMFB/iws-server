from flask import Blueprint

from app.mod_features.models import Feature

mod_features = Blueprint('features', __name__, url_prefix='/v1/features')


@mod_features.route('/', methods=['GET'])
def get_all():
    print 'controller'
    print Feature.query.all()
    return Feature.query.all()
