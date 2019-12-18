# -*- coding: utf-8 -*-
import logging
import xmlrpc.client

_logger = logging.getLogger(__name__)


class Connection(object):
    
    def __init__(self, url):
        self._url = url
        self._common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self._url))

    def trasmit(self, method, *args, **kwargs):
        try:
            response = getattr(self._common, method)(*args)
            _logger.info("Response of method '{}' ⭢ {}".format(method, response))
            return response
        except xmlrpc.client.ProtocolError as err:
            _logger.error(err)

    def authenticate(self, db, user, password, session={}):
        response = self.trasmit('authenticate', db, user, password, session)
        return response
