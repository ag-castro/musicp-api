from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['.centraldobrasil.club']

# mongodb://mp-db:d115e68fc9a342d500b20919fe58955f@dokku-mongo-mp-db:27017/mp_db

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mp-db',
        'HOST': 'dokku-mongo-mp-db',
        'PORT': 27017,
        'USER': 'mp-db',
        'PASSWORD': 'd115e68fc9a342d500b20919fe58955f',

    },
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