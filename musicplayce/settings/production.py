from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['.centraldobrasil.club']

DATABASES = {
    # 'default': {
    #     'ENGINE': 'djongo',
    #     'NAME': 'musicplayce',
    # } mongodb://mp-db:d115e68fc9a342d500b20919fe58955f@dokku-mongo-mp-db:27017/mp_db
    'default': {
        'default': dj_database_url.parse(os.environ.get('MONGO_URL')),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

MEDIA_ROOT = '/storage'

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'https://mp.centraldobrasil.club',
    'https://musicplayce-ui.centraldobrasil.club',
    'https://centraldobrasil.club',
    'https://wwww.centraldobrasil.club',
)