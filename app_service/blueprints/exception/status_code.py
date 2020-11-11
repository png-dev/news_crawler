# -*- coding: utf-8 -*-

'''
Informational responses ( 100 - 199)

Successful responses ( 200 -299)

Redirects  ( 300 - 399)

Client errors ( 400 - 499)

Server errors ( 500 - 599)
'''

HTTP_STATUS_CODES = {
    100: 'Continue',
    101: 'Switching Protocol',
    102: 'Processing',
    103: 'Early Hints',

    200: 'Ok',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi-Status',
    208: 'Already Reported',
    226: 'IM Used',

    300: 'Multiple Choice',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: 'Unused',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',

    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'Uri Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfiable',
    417: 'Expectation Failed ',
    418: 'I am a teapot',
    421: 'Misdirected Request',
    422: 'Unprocessable Entity ',
    423: 'Locked',
    424: 'Failed Dependency',

    500: 'Internal Server Error',
    501: 'Not Implemented ',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiated',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required'
}
