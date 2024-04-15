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
    def withFrameRange(cls, showName: str, shotName: str, startFrame: int, endFrame: int) -> 'Shot':
        instance = cls(showName=showName, shotName=shotName)
        instance.setFrameRange(startFrame=startFrame, endFrame=endFrame)
        return instance

    def __init__(self, showName: str, shotName: str) -> None:
        # store as a map for easy translation to json
        self._map = {
            'name': shotName,
            'showName': showName,
            'startFrame': None,
            'endFrame': None
        }

    # properties

    @property
    def name(self):
        return self._map['name']
    
    @property
    def showName(self):
        return self._map['showName']

    @property
    def startFrame(self):
        return self._map['startFrame']
    
    @property
    def endFrame(self):
        return self._map['endFrame']
    
    @property
    def map(self):
        return self._map

    # public methods

    def frames(self):
        # yielf frames from startFrame to endFrame, inclusively
        for f in range(self.startFrame, self.endFrame + 1):
            yield Frame(f)
    
    def setFrameRange(self, startFrame, endFrame):
        self._map['startFrame'] = startFrame
        self._map['endFrame'] = endFrame

