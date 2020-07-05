import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "jFjhvkGVJjFjV5jFJ8Vv6j5vjKV"

MONGODB_SETTINGS = {     'db': 'test',
    'host': '127.0.0.1',
    'port': 27017 }