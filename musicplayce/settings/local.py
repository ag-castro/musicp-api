from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'musicplayce',
    }
}


CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000',
    'http://localhost:4200',
)