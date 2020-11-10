# -*- coding: utf-8 -*-

import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler


def set_logger_app():
    logger = logging.getLogger('new_crawler_logs')
    file_handler = RotatingFileHandler('../new_crawler_logs.log', backupCount=5)
    handler = logging.StreamHandler()
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s : %(message)s '
            '[in %(module)s: %(pathname)s:%(lineno)d]'
        )
    )
    handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s : %(message)s '
            '[in %(module)s: %(pathname)s:%(lineno)d]'
        )
    )
    logger.addHandler(file_handler)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
