'''
Define the render/ endpoint
Usage:
    <url>/render/<int>
'''

import io

from flask import Blueprint
from flask import jsonify

from render.model.renderer import Renderer
from render.model.shot import Shot

api = Blueprint('fibo_api', __name__)

@api.get('/render/<shot>/<int:startFrame>/<int:endFrame>')
def render(shot, startFrame, endFrame):
    shot = Shot.fromFrameRange(shot, startFrame, endFrame)
    ioStr =  io.StringIO()
    renderer = Renderer.fromMetadataFile(ioStr)
    result = renderer.render(shot)
    return jsonify(result)
