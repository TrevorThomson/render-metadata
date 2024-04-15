'''
Define the render/ endpoint
'''

import flask

from database.model.cassandra import Cassandra
from render.model.shot import Shot

api = flask.Blueprint('shot_api', __name__)

@api.post('/shot')
def postShot():
    data = flask.request.json

    showName = data.get('showname')
    shotName = data.get('shotname')
    startFrame = data.get('startframe')
    endFrame = data.get('endframe')

    shot = Shot.withFrameRange(showName, shotName, startFrame, endFrame)

    flask.current_app.db.openSession()
    jsonshot = flask.json.dumps(shot.map)
    response = flask.current_app.db.write(keyspace=showName, data=jsonshot)
    flask.current_app.db.closeSession()

    return response

@api.get('/show/<showname>/shot/<shotname>')
def getShot(showname, shotname):
    flask.current_app.db.openSession()
    response = flask.current_app.db.read(keyspace=showname, table='shows', key=shotname)
    flask.current_app.db.closeSession()

    return response
