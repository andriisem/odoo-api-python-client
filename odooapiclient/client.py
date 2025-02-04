from . import service_tools


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
        service = service_tools.Connection(self._url, 'common')
        self._uid = service.authenticate(self._db, login, pwd, {})
        return self._uid

    def search(self, model, domain=False, context=None, **kwargs):
        if not context:
            context = {}
        if not kwargs:
            kwargs ={}
        kwargs.update({'context': context})
        service = service_tools.Connection(self._url, 'object')
        response = service.models(self._db, self._uid, self._password, model, 'search', domain or [], **kwargs)
        return response

    def search_read(self, model, domain=False, fields=False, context=None, **kwargs):
        if not context:
            context = {}
        if not kwargs:
            kwargs ={}
        kwargs.update({'context': context})

        service = service_tools.Connection(self._url, 'object')
        response = service.Model(self._db, self._uid, self._password, model, 
                                        'search_read', domain or [],
                                        fields=fields, **kwargs)
        return response
        

    def create(self, model, values, context=None):
        if not context:
            context = {}
        service = service_tools.Connection(self._url, 'object')
        response = service.models(self._db, self._uid, self._password, model, 'create', values, context=context)
        return response
