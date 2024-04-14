
import io
import json
import unittest

from renderer.model.shot import Shot
from renderer.model.renderer import Renderer

class TestRenderer(unittest.TestCase):
    def setUp(self) -> None:
        self.shot = Shot.fromFrameRange('myshot', 101, 110)

    def test_construct(self):
        ioObj = io.StringIO()
        renderer = Renderer.fromMetadataFile(ioObj)
        self.assertTrue(True)
    
    def test_render(self):
        ioObj = io.StringIO()
        renderer = Renderer.fromMetadataFile(ioObj)
        result = renderer.render(self.shot)
        self.assertEqual(result[101]['status'], 'complete')

