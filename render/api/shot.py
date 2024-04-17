'''
Define the render/ endpoint
'''

import flask

from database.model.cassandra import Cassandra
from render.model.shot import Shot

api = flask.Blueprint('shot_api', __name__)

@api.post('/shot')
def postShot():
    data = flask.json.loads(flask.request.json)
    showName = data.get('showname')

    # # debugging
    # shotName = data.get('name')
    # startFrame = data.get('startframe')
    # endFrame = data.get('endframe')
    # shot = Shot.withFrameRange(showName, shotName, startFrame, endFrame)
    # print(f'posted shot: {shot}')
    # # end debugging

    flask.current_app.db.openSession()
    result = flask.current_app.db.write(keyspace=showName, data=flask.request.json)
    flask.current_app.db.closeSession()

    response = flask.make_response('', 200)
    return response

@api.get('/show/<showname>/shot/<shotname>')
def getShot(showname, shotname):
    flask.current_app.db.openSession()
    response = flask.current_app.db.read(keyspace=showname, table='shows', key=shotname)
    flask.current_app.db.closeSession()

    return response
