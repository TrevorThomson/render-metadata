
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

import logging
logging.basicConfig(level=logging.INFO)

def create_service(cassandraAddrs):
    # create and configure the app
    service = flask.Flask(__name__)

    Cassandra.waitFor(cassandraAddrs, timeout=60)

    service.db = Cassandra(cassandraAddrs)

    # register the api endpoints
    service.register_blueprint(render.api.render.api)
    service.register_blueprint(render.api.shot.api)

    return service
