import auth


class Client(object):
    
    def __init__(self, protocol='http', host='localhost', port=8069, dbname=None, ssl=False):
        if ssl:
            protocol, port = 'https', 443
        
        self._host = host
        self._port = port
        self._db = dbname
        self._protocol = protocol
        
        self._url = "{protocol}://{host}:{port}".format(
            protocol=self._protocol, 
            host=self._host, 
            port=self._port
        )

    def authenticate(self, login, pwd):
        self._login, self._password = login, pwd
        service = auth.Connection(self._url)
        self._uid = service.authenticate(self._db, login, pwd, {})
        return self._uid
