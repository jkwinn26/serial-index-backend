"""To use, execute:
manage.py runserver 0.0.0.0:# --settings serializer.local_settings
"""
from serialindex.settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)

