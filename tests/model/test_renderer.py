
import unittest

from render.model.shot import Shot
from render.model.renderer import Renderer

class TestRenderer(unittest.TestCase):
    def setUp(self) -> None:
        self.shot = Shot.withFrameRange('myshow', 'myshot', 101, 110)

    def test_construct(self):
        renderer = Renderer()
        self.assertTrue(True)
    
    def test_render(self):
        renderer = Renderer()
        result = renderer.render(self.shot)
        self.assertEqual(result[101]['status'], 'queued')

