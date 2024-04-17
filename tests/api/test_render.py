
import requests
import unittest
 
# testing how gunicorn will import the service
from render import create_service

class TestRender(unittest.TestCase):
    def setUp(self) -> None:
        # testing how gunicorn wil construct the service
        app = create_service(['localhost'])
        app.testing = True
        self.app = app.test_client()

    def test_render(self):
        data = { 'shotname': 'myshot', 'startframe': 101, 'endframe': 110 }
        response = self.app.post('/render', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['101']['status'], 'queued')

