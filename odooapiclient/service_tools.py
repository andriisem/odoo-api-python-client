# -*- coding: utf-8 -*-
import logging
import xmlrpc.client


class Connection(object):
    
    def __init__(self, url, endpoint):
        self._url = url
        self._endpoint = endpoint
        self._common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/{}'.format(self._url, self._endpoint))

    def trasmit(self, method, *args, **kwargs):
        try:
            response = getattr(self._common, method)(*args)
            return response
        except xmlrpc.client.ProtocolError as err:
            raise err

    def authenticate(self, db, user, password, session={}):
        try:
            response = self.trasmit('authenticate', db, user, password, session)
            return response
        except Exception as err:
            raise err

    def models(self, db, uid, password, model, method, *args, **kwrags):
        try:
            response = self.trasmit('execute_kw', db, uid, password, model, method, args, kwrags)
            return response
        except Exception as err:
            raise err
