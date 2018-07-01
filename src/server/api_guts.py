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

class getFeatures(Resource):
    def get(self):
        conn = db_connect.connect()
        titles = []
        query = conn.execute("select * from feature")
        for c in query:
        	# titles.append([{"title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area}])
        	titles.append({"title": c.title, "description": c.description, "client": c.client, "product_area": c.product_area})
        return jsonify(titles)

api.add_resource(getFeatures, '/api/features2') # Route_1
# # api.add_resource(Tracks, '/tracks') # Route_2
# # api.add_resource(Title_Name, '/title/<title_id>') # Route_3

 
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
 
def make_feature(feature):
    new_feature = {}
    for field in feature:
        if field == 'id':
            new_feature['uri'] = url_for('get_feature', feature_id = feature['id'], _external = True)
        else:
            new_feature[field] = feature[field]
    return new_feature
    
@app.route('/api/features', methods = ['GET'])
def get_features():
    return jsonify( { 'features': map(make_feature, getFeatures())} )
 
@app.route('/api/features/<int:feature_id>', methods = ['GET'])
def get_feature(feature_id):
    feature = filter(lambda t: t['id'] == feature_id, features)
    if len(feature) == 0:
        abort(404)
    return jsonify( { 'feature': make_feature(feature[0]) } )
 
@app.route('/api/features', methods = ['POST'])
def create_feature():
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
def update_feature(feature_id):
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
def delete_feature(feature_id):
    feature = filter(lambda t: t['id'] == feature_id, features)
    if len(feature) == 0:
        abort(404)
    features.remove(feature[0])
    return jsonify( { 'result': True } )

if __name__ == '__main__':
     app.run(port='5002')