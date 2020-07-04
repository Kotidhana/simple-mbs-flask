import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "jFjhvkGVJjFjV5jFJ8Vv6j5vjKV"

MONGODB_SETTINGS = {'db':'mb_system',
    'host':'mongodb://localhost:27017/mb_system'
}