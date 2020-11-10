# -*- coding: utf-8 -*-
import os

DEBUG = True
LOG_LEVEL = 'DEBUG'
SERVER_NAME = None
SERVER_KEY = os.urandom(16)

# Redis
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost')
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)

# DATABASE

DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'news_education')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 27017)
DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '123456a@@')

# PATH
UPLOAD_DIRECTORY_PATH = os.environ.get('UPLOAD_DIRECTORY_PATH', 'files/media/education')
SWAGGER_FILE_PATH = os.environ.get('SWAGGER_FILE_PATH', 'files/swagger/swagger.yaml')
