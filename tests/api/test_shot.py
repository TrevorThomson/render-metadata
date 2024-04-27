
import json
import unittest
 
# testing how gunicorn will import the service
from render import create_service
from render.model.shot import Shot

import logging
logging.basicConfig(level=logging.INFO)

class TestRender(unittest.TestCase):
    def setUp(self) -> None:
        # testing how gunicorn wil construct the service
        app = create_service(['localhost'])
        app.testing = True
        self.app = app.test_client()
    
    def test_postShot(self):
        shot = Shot.withFrameRange('myshow', 'myshot', 101, 110)

        success = self.app.post('/shot', json=shot)
        self.assertTrue(success)
        # self.assertEqual(response.json['101']['status'], 'queued')

