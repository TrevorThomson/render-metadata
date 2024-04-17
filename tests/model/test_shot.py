
import unittest

from render.model.shot import Shot

class TestShot(unittest.TestCase):

    def test_construct(self):
        shot = Shot.withFrameRange('myshow', 'myshot', 101, 110)
        self.assertEqual(shot.startFrame, 101)
        self.assertEqual(shot.endFrame, 110)

    def test_frame(self):
        shot = Shot.withFrameRange('myshow', 'myshot', 101, 101)
        for frame in shot.frames():
            self.assertEqual(frame.number, 101)
