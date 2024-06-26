'''
Define the render/ endpoint
'''

import flask

from database.model.cassandra import Cassandra
from render.model.shot import Shot

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

api = flask.Blueprint('shot_api', __name__)

@api.post('/shot')
def postShot():
    logger.debug(f'request content type: {flask.request.content_type}')
    logger.debug(f'request python type: {type(flask.request.json)}')
    logger.debug(f'request.json: {flask.request.json}')

    data = flask.request.json
    showname = data.get('showname')

    flask.current_app.db.openSession()
    result = flask.current_app.db.write(keyspace=showname, data=flask.request.json)
    flask.current_app.db.closeSession()

    response = flask.make_response('', 200)
    return response

@api.get('/shot/<shotname>/show/<showname>')
def getShot(showname, shotname):
    flask.current_app.db.openSession()
    response = flask.current_app.db.read(keyspace=showname, table='shots', key=shotname)
    flask.current_app.db.closeSession()

    return response
