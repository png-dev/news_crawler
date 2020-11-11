# -*- coding: utf-8 -*-

import logging

_logger = logging.getLogger('new_crawler_logs.log')


class ServiceException(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        res = dict(self.payload or ())
        res['message'] = self.message
        return res


class InvalidUsage(ServiceException):
    status_code = 400


class Unauthorized(ServiceException):
    status_code = 401


class NewsNotFound(ServiceException):
    status_code = 454
