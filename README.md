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

Run the webserver:

* python3 runserver.py

Required modules:
* flask 
* sqlalchemy 
* flask-sqlalchemy
* flask-jsonpify 
* flask-restful
* flask-bootstrap
* flask-migrate
* flask-httpauth
* flask-wtf





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




# Cheatsheet:

On model change:
flask db init
flask db migrate
flask db upgrade

>>> from app import db
>>> from app.models import Feature


db.session.add(Feature(...))
db.session.commit()

>>> f = Feature(title="t2", description="d2", client="c2", client_priority="2", target_date=datetime.datetime(2222, 2, 2), product_area="p2")

f = {"id"=5, title":"t3", "description":"d3", "client":"c3", "product_area":"p3"}

f = {id = 1, title = "t1", description = "d1", client = "c1", product_area = p1"}
g = {id = 2, title = "t2", description = "d2", client = "c2", product_area = p2"}

h = {id = 3, title = "t3", description = "d3", client = "c3", product_area = p3"}