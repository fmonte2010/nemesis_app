# config/testing.py
from .default import *

# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

# SECRET_KEY = '5e04a4955d8878191923e86fe6a0dfb24edb226c87d6c7787f35ba4698afc86e95cae409aebd47f7'

APP_ENV = APP_ENV_TESTING

WTF_CSRF_ENABLED = False

SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@localhost/testing'
