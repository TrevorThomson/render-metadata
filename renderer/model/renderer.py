'''
Simulate a toy rendering service by generating frame metadata
Usage:
# construct a renderer
renderer = Renderer()
# render a shot which will output frame metadata to a 
renderer.render(shot)
'''

import typing

from renderer.model.shot import Shot

class Renderer:
    # constructors
    @classmethod
    def fromMetadataFile(cls, file: typing.IO[str]) -> 'Renderer':
        instance = cls()
        instance._metadata_file = file
        return instance

    def __init__(self) -> None:
        self._metadata_file = None

    # public methods
    def render(self, shot: Shot) -> dict:
        if not self._metadata_file:
            raise AttributeError('Renderer: metadata file undefined')
        result = {}
        for frame in shot.frames():
            frameresult = self._renderFrame(frame)
            result[frame.number] = frameresult
        return result
    
    # private methods
    def _renderFrame(self, frame) -> dict:
        result = {
            'status': 'complete',
            'time': '300'
        }
        return result

