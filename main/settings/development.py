import os
from . import base


API_KEYS = base.API_KEYS
BASE_DIR = base.BASE_DIR
SECRET_KEY = base.SECRET_KEY
DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]

# Application definition
INSTALLED_APPS = base.INSTALLED_APPS + ["debug_toolbar"]
AUTH_USER_MODEL = base.AUTH_USER_MODEL
MIDDLEWARE = base.MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
ROOT_URLCONF = base.ROOT_URLCONF
TEMPLATES = base.TEMPLATES
WSGI_APPLICATION = base.WSGI_APPLICATION
REST_FRAMEWORK = base.REST_FRAMEWORK


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("DATABASE_URL"),
        "PORT": os.environ.get("DATABASE_PORT"),
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
    }
}


# Cache
CACHES = base.CACHES


# Password validation
AUTH_PASSWORD_VALIDATORS = base.AUTH_PASSWORD_VALIDATORS


# JWT
SIMPLE_JWT = base.SIMPLE_JWT


# Internationalization
LANGUAGE_CODE = base.LANGUAGE_CODE
TIME_ZONE = base.TIME_ZONE
USE_I18N = base.USE_I18N
USE_TZ = base.USE_TZ


# Static files (CSS, JavaScript, Images)
STATIC_URL = base.STATIC_URL
MEDIA_URL = base.MEDIA_URL
STATICFILES_DIRS = base.STATICFILES_DIRS
STATIC_ROOT = base.STATIC_ROOT
MEDIA_ROOT = base.MEDIA_ROOT


# CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


# Default primary key field type
DEFAULT_AUTO_FIELD = base.DEFAULT_AUTO_FIELD


# Default Login
LOGIN_REDIRECT_URL = base.LOGIN_REDIRECT_URL
LOGOUT_REDIRECT_URL = base.LOGOUT_REDIRECT_URL


# etc
APPEND_SLASH = base.APPEND_SLASH
