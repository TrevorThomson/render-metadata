
import unittest

from database.model.cassandra import Cassandra

class TestCassandra(unittest.TestCase):

    def test_connect(self):
        db = Cassandra(['localhost'])
        db.openSession()
        db.closeSession()
        self.assertTrue(True)
    
    def test_system_local(self):
        db = Cassandra(['localhost'])
        db.openSession()
        result = db.system_local()
        db.closeSession()
        self.assertTrue(result)

    def test_write(self):
        db = Cassandra(['localhost'])
        db.openSession()
        data = {
            'test': 'testing'
        }
        db.write(keyspace='rendering',data=data)
        db.closeSession()
        self.assertTrue(True)

