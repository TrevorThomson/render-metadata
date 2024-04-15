
'''
Define create_service() function.
Usage:
    service = create_service()
    service.run()
'''

import flask

import render.api.render

from database.model.cassandra import Cassandra

def create_service():
    # create and configure the app
    service = flask.Flask(__name__)

    service.db = Cassandra(['172.18.0.3'])

    # register the api endpoints
    service.register_blueprint(render.api.render.api)

    return service
