
import json
import unittest

from renderer.model.frame import Frame

class TestFrame(unittest.TestCase):

    def test_construct(self):
        frame = Frame(101)
        self.assertEqual(frame.number, 101)
