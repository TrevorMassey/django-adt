"""
Django settings for django_adt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils import timezone
import os
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_URL = 'http://10.10.10.10:8000'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '38m$1477(y^$ujuhhe0du&i6zk0qgy@!c)g=!4al%s&zh3%pm*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'debug_toolbar',
    'django_extensions',
    'fsm_admin',
    'filer',
    'mptt',
    'easy_thumbnails',
    'djcelery',
    'rest_framework_swagger',
    'schedule',

    'swampdragon',

    'accounting',
    'activityfeed',
    'applications',
    'awards',
    'dossiers',
    'games',
    'dkp',
    'publications',
    'users',
    'reviews',
    'polls',
    'notifications',
    'comments',
    'multimedia',
    'event_calendar',
    'frontend',

    'legacy.addict_forum',
    'legacy.addict_logs',
    'legacy.addict_website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'django_adt.urls'

WSGI_APPLICATION = 'django_adt.wsgi.application'

MIGRATION_MODULES = {'filer': 'filer.migrations_django'}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_adt',
        'USER': 'django_adt',
        'PASSWORD': 'django_adt',
    },
    'addict_forum': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'addict_forum',
        'USER': 'root',
        'PASSWORD': 'beer',
    },
    'addict_logs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'addict_logs',
        'USER': 'root',
        'PASSWORD': 'beer',
    },
    'addict_website': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'addict_website',
        'USER': 'root',
        'PASSWORD': 'beer',
    },
}

DATABASE_ROUTERS = ['django_adt.db.routers.LegacyDBRouter', ]

EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 1025


# Celery settings
BROKER_URL = 'redis://localhost:6379/0'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'users.User'

DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('10.10.10.1',)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
}

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timezone.timedelta(days=14),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.jwt.jwt_response_payload_handler',
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': timezone.timedelta(days=7),
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'INFO',
            'class': 'django.utils.log.NullHandler',
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logfile.log"),
            'maxBytes': 1024*1024*10,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
        'games.signals': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)



# Swammpdragon Settings

SWAMP_DRAGON_CONNECTION = ('django_adt.connections.JWTDataConnection', '/data')

SWAMP_DRAGON_HOST = '0.0.0.0'
SWAMP_DRAGON_PORT = 9080

DRAGON_URL = 'http://127.0.0.1:9080/'

SWAGGER_SETTINGS = {
    'api_version': '1.0',
    'api_path': '/api/',
    'doc_expansion': 'none',
}

class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

import sys
TESTS_IN_PROGRESS = False

if 'test' in sys.argv[1:] or 'jenkins' in sys.argv[1:]:
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
    DEBUG = False
    TEMPLATE_DEBUG = False
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = DisableMigrations()

    for key in DATABASES.keys():
        DATABASES[key]['ENGINE'] = 'django.db.backends.sqlite3'