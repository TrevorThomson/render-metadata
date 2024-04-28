'''
Toy wrapper around an Apache Cassandra database
'''

# import cassandra
import time

from cassandra.cluster import Cluster
from cassandra import RequestExecutionException

import logging
logger = logging.getLogger(__name__)
cassandra_logger = logging.getLogger('cassandra')
# block logger messages from cassandra module
cassandra_logger.setLevel(logging.CRITICAL + 10)

class Cassandra:
    '''
    Class to communicate with a Cassandra cluster
    Data model (WIP):
    - keyspace : show name
    - tables:
        - shots: primary key is shot name -- unique per show for this simple example
        - frames: primary key (shot, frame)
    '''

    def __init__(self, ipAddresses: list) -> None:
        self._cluster = Cluster(ipAddresses)
        self._session = None
    
    @classmethod
    def waitFor(cls, ipAddresses: list, timeout: int):
        startTime = time.time()
        while True:
            try:
                logger.info(f'Waiting for cluster at {ipAddresses}...')
                cluster = Cluster(ipAddresses)
                session = cluster.connect()
                session.execute('SELECT release_version FROM system.local')
                session.shutdown
                logger.info(f'Cluster available.')
                return True
            except:
                if time.time() - startTime >= timeout:
                    raise TimeoutError(f'Cluster unavailable.')
                else:
                    time.sleep(2)

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

    def writeShot(self, keyspace: str, shot: dict) -> bool:
        try:
            self._session.execute(
                query=f'''
                    CREATE KEYSPACE IF NOT EXISTS {keyspace} 
                    WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};
                ''')
            self._session.execute(
                query=f'''
                    CREATE TABLE IF NOT EXISTS {keyspace}.shots (
                        name TEXT,
                        startframe INT,
                        endframe INT,
                        PRIMARY KEY (name)
                    );
            ''')
        except RequestExecutionException as e:
            # re-raise error for now
            # todo: design error handling
            raise 

    def system_local(self) -> str:
        result = self._session.execute(
            '''
            SELECT * FROM system.local;
            '''
        )
        return bool(result)
