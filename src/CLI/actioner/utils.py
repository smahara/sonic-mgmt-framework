import urllib3
import httplib
import socket
class UnixHTTPConnection(httplib.HTTPConnection, object):

    def __init__(self, socket_path, timeout=60):
        """Create an HTTP connection to a unix domain socket

        :param socket_path: The path to the Unix domain socket
        :param timeout: Number of seconds to timeout the connection
        """
        super(UnixHTTPConnection, self).__init__('localhost', timeout=timeout)
        self.socket_path = socket_path
        self.sock = None

    def __del__(self):  # base class does not have d'tor
        if self.sock:
            self.sock.close()


    def connect(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        sock.connect(self.socket_path)
        self.sock = sock



class UnixHTTPConnectionPool(urllib3.poolmanager.PoolManager):
# class UnixHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):

    def __init__(self, socket_path, timeout=60):
        """Create a connection pool using a Unix domain socket

        :param socket_path: The path to the Unix domain socket
        :param timeout: Number of seconds to timeout the connection
        """
        super(UnixHTTPConnectionPool, self).__init__('localhost', timeout=timeout)
        self.socket_path = socket_path

    def _new_conn(self):
        return UnixHTTPConnection(self.socket_path, self.timeout)