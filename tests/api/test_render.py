
import unittest

# testing how gunicorn will import the service
from render import create_service

class TestRender(unittest.TestCase):
    def setUp(self) -> None:
        # testing how gunicorn wil construct the service
        app = create_service()
        app.testing = True
        self.app = app.test_client()

    def test_render(self):
        result = self.app.get('/render/myshot/101/110')
        self.assertEqual(result.get_json()['101']['status'], 'complete')

