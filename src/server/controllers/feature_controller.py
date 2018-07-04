from flask import Flask, jsonify, abort, request, make_response, url_for, \
	Blueprint, render_template, flash, g, session, redirect
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api
# from flask_apiblueprint import APIBlueprint

from server import app 
from server import db


# Take app and auth out of app and put them somewhere else?
# from app import app
# from app import auth

from server.models.feature import Feature

fapi = Blueprint('fapi', __name__, url_prefix='/api')
# app.register_blueprint(fapi)
print "CONTROLLER"
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from json import dumps


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "feature_request.db"))

# db_connect = create_engine(database_file)

# app = Flask(__name__)
# api = Api(app)
# conn = db_connect.connect()
# auth = HTTPBasicAuth()


# @auth.get_password
# def get_password(username):
#     if username == 'iws':
#         return 'pass'
#     return None

# @app.errorhandler(400)
# def bad_request(error):
# 	return make_response(jsonify( { 'error': 'Bad request' } ), 400)

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog	
 
# @app.errorhandler(404)
# def not_found(error):
# 	return make_response(jsonify( { 'error': 'Not found' } ), 404)

# @app.route('/api/features', methods = ['GET'])
@fapi.route('/features', methods = ['GET'])
def query_all():
	print "QUERRRY ALLLLLL"
	# TODO: Come back and redo this the right way.
	conn = db_connect.connect()
	query = conn.execute("select * from feature")
	all_features = []
	for c in query:
		# titles.append([{"title": c.title, "description": c.description, "client": c.client, "client_priority": c.client_priority, "target_date": c.target_date, "product_area": c.product_area}])
		all_features.append({"id": c.id, "title": c.title, "description": c.description, "client": c.client, "product_area": c.product_area})
	all_features = {"features": all_features}
	resp = make_response(jsonify(all_features))
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp



# @app.route('/api/features', methods = ['POST'])
def create():
	conn = db_connect.connect()
	if not request.json or not 'title' in request.json:
		abort(400)
	# TODO: Change id to max(id) + 1

	f = Feature(title= request.json['title'], description= request.json.get('description', "None"), client= request.json.get('client', "None"), product_area= request.json.get('product_area', "None"))
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
 
# @app.route('/api/features/<int:feature_id>', methods = ['PUT'])
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

# @app.route('/api/features/<int:feature_id>', methods = ['DELETE'])
def delete_one(feature_id):
	# TODO: Make 
	feature = filter(lambda t: t['id'] == feature_id, features)
	if len(feature) == 0:
		abort(404)
	features.remove(feature[0])
	return jsonify( { 'result': True } )

# @app.route('/api/features/<int:feature_id>', methods = ['GET'])
# def get_one():
# 	# TODO: Make or delete this
# 	conn = db_connect.connect()
# 	query = conn.execute("select * from feature")

# 	feature = filter(lambda t: t['id'] == feature_id, features)
# 	if len(feature) == 0:
# 		abort(404)
# 	return jsonify( { 'feature': make_feature(feature[0]) } )		


	# class Feature(db.Model):
#     title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

#     def __repr__(self):
#         return "<Title: {}>".format(self.title)


# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.form:
#         feature_title = Feature(title=request.form.get("title"))
#         db.session.add(feature_title)
#         db.session.commit()
#     features = Feature.query.all()
#     return render_template("home.html", features=features)

# @app.route("/update", methods=["POST"])
# def update():
#     newtitle = request.form.get("newtitle")
#     oldtitle = request.form.get("oldtitle")
#     feature = Feature.query.filter_by(title=oldtitle).first()
#     feature.title = newtitle
#     db.session.commit()
#     return redirect("/")

# @app.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     feature = Feature.query.filter_by(title=title).first()
#     db.session.delete(feature)
#     db.session.commit()
#     return redirect("/")