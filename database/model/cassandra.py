'''
Toy wrapper around an Apache Cassandra database
'''

from cassandra.cluster import Cluster

class Cassandra:
    '''
    Class to communicate with a Cassandra cluster
    '''

    def __init__(self, ipAddresses: list) -> None:
        self._cluster = Cluster(ipAddresses)
        self._session = None

    @property
    def hasSession(self) -> bool:
        return self._session != None

    def openSession(self) -> None:
        '''
        open a session independly of the write method to ensure
        we're not thrashing (opening too many short-lived sessions)
        '''
        if self._session:
            raise Exception('Session already created!')
        self._session = self._cluster.connect()
    
    def closeSession(self) -> None:
        if self._session:
            self._session.shutdown()
            self._session = None

    def write(self, keyspace: str, data: dict) -> bool:
        result = self._session.execute(
            trace=True,
            query=f'''
                CREATE KEYSPACE IF NOT EXISTS {keyspace} 
                WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};
            ''')

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

        return bool(result)

    def system_local(self) -> str:
        result = self._session.execute(
            '''
            SELECT * FROM system.local;
            '''
        )
        return bool(result)
