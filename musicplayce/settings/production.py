from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['.centraldobrasil.club']

DATABASES = {

    'default': {
        'default': dj_database_url.parse(os.environ.get('MONGO_URL')),
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