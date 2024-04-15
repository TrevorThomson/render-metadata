'''
Define the write/ endpoint
Usage:
    <url>/write/<data>
'''

import flask

from database.model.cassandra import Cassandra

api = flask.Blueprint('startSession_api', __name__)

@api.post('/startSession')
def startSession():
    db = Cassandra(['127.0.0.1',])
    db.openSession()

    flask.session['db'] = db

    return flask.make_response('', 200)
