
import unittest

from database.model.cassandra import Cassandra

class TestCassandra(unittest.TestCase):

    def test_construct(self):
        db = Cassandra('127.0.0.1', 9042)
        self.assertTrue(True)
    
    def test_write(self):
        db = Cassandra('127.0.0.1', 9042)
        data = {
            'test': 'testing'
        }
        db.write(data)
        self.assertTrue(True)

