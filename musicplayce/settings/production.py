from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.centraldobrasil.club']

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'musicplayce',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000',
    'http://localhost:4200',
)