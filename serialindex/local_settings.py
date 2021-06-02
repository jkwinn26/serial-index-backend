"""To use, execute:
manage.py runserver 0.0.0.0:# --settings serializer.local_settings
"""
from serialindex.settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'interface',
#         'HOST': 'database.dev.blaze.rrd.com',
#         'PORT': 3306,
#         'USER': 'blaze',
#         'PASSWORD': 'Flam1ngCarr0t!',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#             'charset': 'utf8mb4',
#         },
#     }
# }

# BLAZE_API = {
#     'domain': 'api.dev.blaze.rrd.com'
# }
