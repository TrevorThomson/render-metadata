'''
Define the render/ endpoint
'''

from flask import Blueprint
from flask import jsonify
from flask import request

from render.model.renderer import Renderer
from render.model.shot import Shot

import logging
logger = logging.getLogger(__name__)

api = Blueprint('render_api', __name__)

@api.post('/render')
def render():
    data = request.json

    showName = data.get('showname')
    shotName = data.get('shotname')
    startFrame = data.get('startframe')
    endFrame = data.get('endframe')

    shot = Shot.withFrameRange(showName, shotName, startFrame, endFrame)
    renderer = Renderer()
    result = renderer.render(shot)

    return jsonify(result), 200
