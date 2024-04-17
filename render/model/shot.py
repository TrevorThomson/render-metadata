'''
Toy representation of a shot to be rendered
Usage:
# construct a shot
shot = Shot()
# set the frame range
shot.setFrameRange(startFrame, endFrame)
'''

from render.model.frame import Frame

class Shot(dict):
    # constructors

    @classmethod
    def withFrameRange(cls, showName: str, shotName: str, startFrame: int, endFrame: int) -> 'Shot':
        instance = cls(showName=showName, shotName=shotName)
        instance.setFrameRange(startFrame=startFrame, endFrame=endFrame)
        return instance

    def __init__(self, showName: str, shotName: str) -> None:
        # store as a map for easy translation to json
        super().__init__()
        self['name'] = shotName
        self['showname'] = showName

    # properties

    @property
    def name(self):
        return self['name']
    
    @property
    def showName(self):
        return self['showname']

    @property
    def startFrame(self):
        return self['startframe']
    
    @property
    def endFrame(self):
        return self['endframe']
    
    # public methods

    def frames(self):
        # yielf frames from startFrame to endFrame, inclusively
        for f in range(self.startFrame, self.endFrame + 1):
            yield Frame(f)
    
    def setFrameRange(self, startFrame, endFrame):
        self['startframe'] = startFrame
        self['endframe'] = endFrame

