# "iws-server" Feature Request App

This site provides an app to keep track of "feature requests", which are requests for a new feature that will be added onto an existing piece of software. This assumes that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature. The fields will be:

* Title: A short, descriptive name of the feature request.
* Description: A long description of the feature request.
* Client: A selection list of clients (use "Client A", "Client B", "Client C")
* Client Priority: A numbered priority according to the client (1...n). Client Priority numbers should not repeat for the given client, so if a priority is set on a new feature as "1", then all other feature requests for that client should be reordered.
* Target Date: The date that the client is hoping to have the feature.
* Product Area: A selection list of product areas (use 'Policies', 'Billing', 'Claims', 'Reports')


# Hello!

In order to get this up and runnin' locally, please make sure that you have the following installed:

* Python 3.0+
(using bower:)
* jquery
* knockoutjs

Required modules:
* flask 
* sqlalchemy 
* sqlalchemy_utils
* flask-sqlalchemy
* flask-migrate
* flask-httpauth
* flask-cors
* flask-restful
* flask-bootstrap
* flask-wtf

bower install jquery-editable-select
bower install moment

Run the api:
* python3 run.py

Run the webserver:
* python3 run_webapp.py

Note that Chrome does not support localhost CORS requests. Use Firefox, set --disable-web-security flag when opening Chrome, or install the "Allow-Control-Allow-Origin: * Chrome Extension": https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi
or similar CORS extension.


Enjoy! :)

Current tasks:

- [x] Get Started
- [x] Set up repos, git flow, deployments, etc.
- [ ] Add in testing suites
- [ ] Small Bugfixes
- [ ] CI, etc.

- [x] Build in full logic
- [x] Build out the Feature Models
- [x] Add in priority lists logic
- [x] Add all to HTML

- [x] Decouple logic server and client
- [x] Make logic server, independent of client
- [x] Build API requsts on logic server
- [x] Link DOM and CRUD to API requests
- [x] Update Readme

- [x] Make it look pretty
- [x] Configure AWS
- [ ] Host on AWS, set up automated deployments
