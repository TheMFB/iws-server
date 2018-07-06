from flask import Blueprint, jsonify, make_response

from app.mod_features.models import Feature

mod_features = Blueprint('features', __name__, url_prefix='/v1/features')


@mod_features.route('/', methods=['GET'])
def get_all():
    print 'controller'
    feature_query = Feature.query.all()
    all_features = []
    for c in feature_query:
        all_features.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "clien_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area})
    featuring_json_derulo = jsonify(all_features)
    print "featuring_json_derulo"
    print featuring_json_derulo
    resp = make_response(featuring_json_derulo)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
