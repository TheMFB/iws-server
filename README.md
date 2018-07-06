# "iws-server" Feature Request App

This site provides an app to keep track of "feature requests", which are requests for a new feature that will be added onto an existing piece of software. This assumes that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature. The fields will be:

* Title: A short, descriptive name of the feature request.
* Description: A long description of the feature request.
* Client: A selection list of clients (use "Client A", "Client B", "Client C")
* Client Priority: A numbered priority according to the client (1...n). Client Priority numbers should not repeat for the given client, so if a priority is set on a new feature as "1", then all other feature requests for that client should be reordered.
* Target Date: The date that the client is hoping to have the feature.
* Product Area: A selection list of product areas (use 'Policies', 'Billing', 'Claims', 'Reports')


# TODO: Add a detailed description on how to get this up and running!!

Hello!

In order to get this up and runnin' locally, please make sure that you have the following installed:

* Python 3.0+
(using bower:)
* jquery
* knockoutjs

Make a new database:

Open python3 in the web-app directory, and run create_db.py

Run the api:
* python3 run_api

Run the webserver:

* python3 run_webapp.py

Note that Chrome does not support localhost CORS requests. Use Firefox, set --disable-web-security flag when opening Chrome, or install the "Allow-Control-Allow-Origin: * Chrome Extension": https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi
or similar CORS extension.



Required modules:
* flask 
* sqlalchemy 
* flask-sqlalchemy
* flask-jsonpify  X
* flask-restful
* flask-bootstrap
* flask-migrate
* flask-httpauth
* flask-wtf
* flask-apiblueprint

flask, sqlalchemy, flask-alchemy, flask-restful, flask-bootstrap, flask-migrate, flask-httpauth, flask-wtf



Enjoy! :)

Current tasks:

- [x] Get Started
- [x] Set up repos, git flow, deployments, etc.
- [ ] Add in testing suites

- [ ] Build in full logic
- [ ] Build out the Feature Models
- [ ] Add in priority lists logic
- [ ] Add all to HTML

- [ ] Decouple logic server and client
- [ ] Make logic server, independent of client
- [ ] Build API requsts on logic server
- [ ] Link DOM and CRUD to API requests
- [ ] Update Readme

- [ ] Make it look pretty
- [x] Configure AWS
- [ ] Host on AWS, set up automated deployments

__________________________________________________

		# TODO: Add a random string module(shortid.generate - as type in the models) (Also, pull all of these into a blueprints/routes file, no class)
		
		
		
		
		
		
		# run puts on everything that's changed (or all of it, based on jquery) - to put (or update) request which can change just the parts that have changed. Do it every time.
			 # Save this for last, mockup if we need. put_many/update_many.
		# first pull the models and controller.










* Controller
	all decorated methods goes into here. (features.py)
	imports the models it needs
* Routes
	all addresses should be pluraled
* db.py
	hosts the db info so that we only call db_connect.connect() once.
	create statements can go there. ? abstracted querries.


__________________________________________________



# Cheatsheet:

On model change:
flask db init
flask db migrate
flask db upgrade

>>> from app import db
>>> from app.models.feature_model import Feature



>>> f = Feature(title="t2", description="d2", client="c2", client_priority="2", target_date=datetime.datetime(2222, 2, 2), product_area="p2")

f = Feature(id="1", title="t2", description="d2", client="c2", product_area="p2")

f = {"id"=5, title":"t3", "description":"d3", "client":"c3", "product_area":"p3"}


f = Feature(id="1", title="t1", description="d1", client="c1", product_area="p1")
g = Feature(id = 2, title = "t2", description = "d2", client = "c2", product_area = "p2")

h = Feature(id = "1", title = "t3", description = "d3", client = "c3", product_area = "p3")

db.create_all()
db.session.add(Feature(...))
db.session.commit()

db.session.close()

curl -i http://127.0.0.1:5002/api/features

_______________________________
~/dev/iws/iws-server/src/web-app$ python3 run_webapp.py
~/dev/iws/iws-server/src/server$ python3 run_api.py


		# TODO: Add a random string module(shortid.generate - as type in the models) (Also, pull all of these into a blueprints/routes file, no class)
		# All decorated mehods into a controllers folder, features.py
		# models folder, and put Feature file into it.
		# controller will import the models it needs. (Kind of like Oshen)
		# db.py for db_connect.connect(). only do this once. 
		# class should be Feature and into models. feature.py
		# everythin app.route needs to be moved. always plural the addresses.
		# db.py should be connected there. select, create statements can go there.
		# run puts on everything that's changed (or all of it, based on jquery) - to put (or update) request which can change just the parts that have changed. Do it every time.
			 # Save this for last, mockup if we need. put_many/update_many.
		# first pull the models and controller.