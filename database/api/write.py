'''
Define the write/ endpoint
Usage:
    <url>/write/<data>
'''

from flask import Blueprint
from flask import make_response

from database.model.cassandra import Cassandra

api = Blueprint('write_api', __name__)

@api.get('/write/<data>')
def write(data):
    db = Cassandra('127.0.0.1', 9042)
    db.write(data)
    response = make_response('', 200)
    return response
