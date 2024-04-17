
'''
Define create_service() function.
Usage:
    service = create_service()
    service.run()
'''

import flask

import render.api.render
import render.api.shot

from database.model.cassandra import Cassandra

def create_service(ipAddresses):
    # create and configure the app
    service = flask.Flask(__name__)

    service.db = Cassandra(ipAddresses)

    # register the api endpoints
    service.register_blueprint(render.api.render.api)
    service.register_blueprint(render.api.shot.api)

    return service
