'''
Toy representation of a frame to be rendered
Usage:
# construct a frame
frame = Frame(frameNumber)
'''

import json

class Frame:
    def __init__(self, frameNumber) -> None:
        self._number = frameNumber

    @property
    def number(self):
        return self._number
