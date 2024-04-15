'''
Toy wrapper around an Apache Cassandra database
'''

from cassandra.cluster import Cluster

class Cassandra:
    '''
    Class to communicate with a Cassandra cluster
    '''
    def __init__(self, ipAddresses: list) -> None:
        # self._cluster = Cluster(ipAddresses)
        # self._session = None
        pass

    def openSession(self) -> None:
        '''
        open a session independly of the write method to ensure
        we're not thrashing (opening too many short-lived sessions)
        '''
        # self._session = self._cluster.connect()
        pass

    def write(self, keyspace: str, data: dict) -> None:
        print(f'keyspace: {keyspace}')
        print(f'data: {data}')
        # self._session.execute(f'''
        #     CREATE KEYSPACE IF NOT EXISTS {keyspace} 
        #     WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};
        # ''')
        # self._session.execute(f'''
        #     CREATE TABLE IF NOT EXISTS {keyspace}.frames (
        #         id UUID PRIMARY KEY,
        #         frame_name TEXT,
        #         frame_width INT,
        #         frame_height INT,
        #         frame_format TEXT,
        #         frame_size_in_bytes INT
        #     );
        # ''')

