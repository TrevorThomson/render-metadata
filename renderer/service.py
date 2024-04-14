
'''
Define create_service() function.
Usage:
    service = create_service()
    service.run()
'''

import flask

import renderer.api.render

def create_service():
    # create and configure the app
    service = flask.Flask(__name__)

    # register the api endpoints
    service.register_blueprint(renderer.api.render.api)

    return service
