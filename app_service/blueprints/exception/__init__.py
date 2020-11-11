# -*- coding:utf-8 -*-
import logging

from flask import (Blueprint, make_response, jsonify)
from werkzeug.exceptions import HTTPException

from .exception import *

_logger = logging.getLogger('new_crawler_logs.log')

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(ServiceException)
def handle_service_exception(error):
    res = make_response(jsonify(error.to_dict()))
    res.status_code = error.status_code
    return res


@error_handler.app_errorhandler(ValueError)
def handle_value_error(error):
    data = {'message': error}
    res = make_response(jsonify(data))
    res.status_code = 404
    return res
