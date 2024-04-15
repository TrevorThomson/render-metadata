
import json
import unittest
 
# testing how gunicorn will import the service
from render import create_service
from render.model.shot import Shot

class TestRender(unittest.TestCase):
    def setUp(self) -> None:
        # testing how gunicorn wil construct the service
        app = create_service()
        app.testing = True
        self.app = app.test_client()

    def test_postShot(self):
        shot = Shot.withFrameRange('myshow', 'myshot', 101, 110)
        jsonshot = json.dumps(shot.map)

        response = self.app.post('/shot', json=jsonshot)
        print(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['101']['status'], 'queued')

