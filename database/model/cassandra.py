'''
Toy wrapper around an Apache Cassandra database
'''

from cassandra.cluster import Cluster

class Cassandra:
    def __init__(self, ipAddress, port) -> None:
        # connect to cluster and start session (w/keyspace)
        pass

    def write(self, data: dict) -> None:
        # map data elements to table schema
        pass
