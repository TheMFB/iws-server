from flask import Flask, jsonify, abort, request, make_response, url_for

from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth