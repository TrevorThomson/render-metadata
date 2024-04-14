'''
Simulate a toy rendering service by generating frame metadata
Usage:
# construct a renderer
renderer = Renderer()
# render a shot which will output frame metadata to a 
renderer.render(shot)
'''

import typing

from render.model.shot import Shot

class Renderer:
    # constructors
    def __init__(self) -> None:
        pass

    # public methods
    def render(self, shot: Shot) -> dict:
        result = {}
        for frame in shot.frames():
            frameresult = self._renderFrame(frame)
            result[frame.number] = frameresult
        return result
    
    # private methods
    def _renderFrame(self, frame) -> dict:
        result = {
            'status': 'queued'
        }
        return result

