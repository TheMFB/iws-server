from flask import Blueprint, jsonify, make_response, request

from app.mod_features.models import Feature, get_all, get_client_list, add, update, remove, remove_all, get_clients

import datetime

mod_features = Blueprint('features', __name__, url_prefix='/v1/features')


@mod_features.route('/', methods=['GET'])
def get_all_features():
    featuring_json_derulo = jsonify(get_all())
    resp = make_response(featuring_json_derulo)
    return resp

@mod_features.route('/clients/', methods=['GET'])
def get_all_clients():
    resp = make_response(jsonify(get_client_list()))
    return resp

@mod_features.route('/clients/filter/<client_name>', methods=['GET'])
def get_feature_of_client(client_name):
    resp = make_response(jsonify(get_clients(client_name)))
    return resp

@mod_features.route('/', methods = ['POST'])
def create_feature():
	# if not request.json or not 'title' in request.json:
	# 	abort(400)
	f = Feature(\
		title= request.json.get('title', "None"), \
		description= request.json.get('description', "None"), \
		client= request.json.get('client', "None"), \
		client_priority= request.json.get('client_priority', 0), \
		target_date= datetime.datetime(\
			request.json.get('target_date_year', datetime.date.today().year), \
			request.json.get('target_date_month', datetime.date.today().month), \
			request.json.get('target_date_day', datetime.date.today().day)), \
		product_area= request.json.get('product_area', "None")\
		)
	return add(f)

@mod_features.route('/update/<feature_id>', methods = ['POST'])
def update_feature(feature_id):
	content = request.json
	# content = {
	# 	'title': request.json.get('title', "None"),
	# 	'description': request.json.get('description', "None"),
	# 	'client': request.json.get('client', "None"),
	# 	'client_priority': request.json.get('client_priority', 0),
	# 	'target_date': datetime.datetime(
	# 		request.json.get('target_date_year', datetime.date.today().year),
	# 		request.json.get('target_date_month', datetime.date.today().month),
	# 		request.json.get('target_date_day', datetime.date.today().day)),
	# 	'product_area': request.json.get('product_area', "None")
	# 	}
	return update(feature_id, content)

@mod_features.route('/<feature_id>', methods = ['DELETE'])
def remove_feature(feature_id):
	return remove(feature_id)

@mod_features.route('/all', methods = ['DELETE'])
def remove_all_features():
	return remove_all()
