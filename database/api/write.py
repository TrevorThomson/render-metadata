'''
Define the write/ endpoint
Usage:
    <url>/write/<data>
'''

import flask

from database.model.cassandra import Cassandra

api = flask.Blueprint('write_api', __name__)

@api.put('/write/<data>')
def write(data):
    db = flask.session.get('db')
    db.write(data)

    return flask.make_response('', 200)
