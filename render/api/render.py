'''
Define the render/ endpoint
'''

from flask import Blueprint
from flask import jsonify
from flask import request

from render.model.renderer import Renderer
from render.model.shot import Shot

api = Blueprint('render_api', __name__)

@api.post('/render')
def render():
    data = request.json

    shotName = data.get('shotname')
    startFrame = data.get('startframe')
    endFrame = data.get('endframe')

    shot = Shot.fromFrameRange(shotName, startFrame, endFrame)
    renderer = Renderer()
    result = renderer.render(shot)
    return jsonify(result), 200
