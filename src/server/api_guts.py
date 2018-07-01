import os

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from app.models import Feature

# from flask.ext.jsonpify import jsonify

project_dir = os.path.dirname(os.path.abspath(__file__))
# src_dir = os.path.dirname(project_dir)
# print src_dir
database_file = "sqlite:///{}".format(os.path.join(project_dir, "feature_request.db"))

db_connect = create_engine(database_file)

app = Flask(__name__)
api = Api(app)
conn = db_connect.connect()
# conn = db_connect.connect()
# features = conn.execute("select * from feature")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
 
class Features(Resource):
	@app.route('/api/features', methods = ['GET'])
	def get_all():
	    conn = db_connect.connect()
	    all_features = []
	    query = conn.execute("select * from feature")
	    for c in query:
	    	# titles.append([{"title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area}])
	    	all_features.append({"title": c.title, "description": c.description, "client": c.client, "product_area": c.product_area})
	    return jsonify(all_features)

	@app.route('/api/features', methods = ['GET'])
	def get_one():
		# TODO: Make or delete this.
	    conn = db_connect.connect()
	    query = conn.execute("select * from feature")

	    feature = filter(lambda t: t['id'] == feature_id, features)
	    if len(feature) == 0:
	        abort(404)
	    return jsonify( { 'feature': make_feature(feature[0]) } )	    

	@app.route('/api/features', methods = ['POST'])
	def create(feature):
	    conn = db_connect.connect()
	    # TODO: Make 
	    query = conn.execute("select * from feature")
	    for c in query:
	    	# titles.append([{"title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area}])
	    	titles.append({"title": c.title, "description": c.description, "client": c.client, "product_area": c.product_area})

	    # new_feature = {}
	    # for field in feature:
	    #     if field == 'id':
	    #         new_feature['uri'] = url_for('get_feature', feature_id = feature['id'], _external = True)
	    #     else:
	    #         new_feature[field] = feature[field]

	    # return new_feature	    

	    if not request.json or not 'title' in request.json:
	        abort(400)
	    feature = {
	        'id': features[-1]['id'] + 1,
	        'title': request.json['title'],
	        'description': request.json.get('description', ""),
	        'done': False
	    }
	    features.append(feature)
	    return jsonify( { 'feature': make_feature(feature) } ), 201
	 
	@app.route('/api/features/<int:feature_id>', methods = ['PUT'])
	def update_one(feature_id):
		# TODO: Make 
	    feature = filter(lambda t: t['id'] == feature_id, features)
	    if len(feature) == 0:
	        abort(404)
	    if not request.json:
	        abort(400)
	    if 'title' in request.json and type(request.json['title']) != unicode:
	        abort(400)
	    if 'description' in request.json and type(request.json['description']) is not unicode:
	        abort(400)
	    if 'done' in request.json and type(request.json['done']) is not bool:
	        abort(400)
	    feature[0]['title'] = request.json.get('title', feature[0]['title'])
	    feature[0]['description'] = request.json.get('description', feature[0]['description'])
	    feature[0]['done'] = request.json.get('done', feature[0]['done'])
	    return jsonify( { 'feature': make_feature(feature[0]) } )
    
	@app.route('/api/features/<int:feature_id>', methods = ['DELETE'])
	def delete_one(feature_id):
		# TODO: Make 
	    feature = filter(lambda t: t['id'] == feature_id, features)
	    if len(feature) == 0:
	        abort(404)
	    features.remove(feature[0])
	    return jsonify( { 'result': True } )


if __name__ == '__main__':
     app.run(port='5002')