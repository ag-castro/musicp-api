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
    'https://mp.centraldobrasil.club',
    'https://musicplayce-ui.centraldobrasil.club',
    'https://centraldobrasil.club',
    'https://wwww.centraldobrasil.club',
)