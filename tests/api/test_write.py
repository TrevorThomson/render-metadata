
import json
import unittest

# testing how gunicorn will import the service
from database import create_service

class TestWrite(unittest.TestCase):
    def setUp(self) -> None:
        # testing how gunicorn wil construct the service
        app = create_service()
        app.testing = True
        self.app = app.test_client()

    def test_write(self):
        data = {
            'test': 'testing'
        }
        jsonStr = json.dumps(data)
        response = self.app.get(f'/write/{jsonStr}')
        self.assertEqual(response.status_code, 200)

