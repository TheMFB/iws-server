import os

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from json import dumps
from app.models import Feature
from app import db

# from flask.ext.jsonpify import jsonify

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "feature_request.db"))

db_connect = create_engine(database_file)

app = Flask(__name__)
api = Api(app)
conn = db_connect.connect()

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not found' } ), 404)
 
class Features(Resource):
	@app.route('/api/features', methods = ['GET'])
	def get_all():
		l, features = Features.query_all()
		return features

	def query_all():
		# TODO: Come back and redo this the right way.
		conn = db_connect.connect()
		all_features = []
		query = conn.execute("select * from feature")
		total = 0
		for c in query:
			total += 1
			# titles.append([{"title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area}])
			all_features.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "product_area": c.product_area})
		features = jsonify(all_features)
		return total, features

	@app.route('/api/feature', methods = ['GET'])
	def get_one():
		# TODO: Make or delete this
		conn = db_connect.connect()
		query = conn.execute("select * from feature")

		feature = filter(lambda t: t['id'] == feature_id, features)
		if len(feature) == 0:
			abort(404)
		return jsonify( { 'feature': make_feature(feature[0]) } )		

	@app.route('/api/features', methods = ['POST'])
	def create():
		conn = db_connect.connect()
		l, features = Features.query_all()
		if not request.json or not 'title' in request.json:
			abort(400)
		# TODO: Change id to max(id) + 1
		f = Feature(id= l + 1, title= request.json['title'], description= request.json.get('description', "None"), client= request.json.get('client', "None"), product_area= request.json.get('product_area', "None"))
		Session = sessionmaker(bind=db_connect)
		session = Session()
		session.add(f)
		session.commit()
		return 'true', 201

	def make():
		new_feature = {}
		for field in feature:
			if field == 'id':
				new_feature['uri'] = url_for('get_feature', feature_id = feature['id'], _external = True)
			else:
				new_feature[field] = feature[field]

		return new_feature
	 
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