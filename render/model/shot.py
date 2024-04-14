'''
Toy representation of a shot to be rendered
Usage:
# construct a shot
shot = Shot()
# set the frame range
shot.setFrameRange(startFrame, endFrame)
'''

from render.model.frame import Frame

class Shot:
    # constructors
    @classmethod
    def fromFrameRange(cls, name: str, startFrame: int, endFrame: int) -> 'Shot':
        instance = cls(name)
        instance.setFrameRange(startFrame=startFrame, endFrame=endFrame)
        return instance

    def __init__(self, name: str) -> None:
        self._name = name
        self._startFrame = None
        self._endFrame = None

    # properties
    @property
    def name(self):
        return self._name

    @property
    def startFrame(self):
        return self._startFrame
    
    @property
    def endFrame(self):
        return self._endFrame

    # generator method
    def frames(self):
        # yielf frames from startFrame to endFrame, inclusively
        for f in range(self._startFrame, self._endFrame + 1):
            yield Frame(f)
    
    # public methods
    def setFrameRange(self, startFrame, endFrame):
        self._startFrame = startFrame
        self._endFrame = endFrame

