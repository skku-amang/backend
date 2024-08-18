import os
from . import base


BASE_DIR = base.BASE_DIR
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = base.INSTALLED_APPS
AUTH_USER_MODEL = base.AUTH_USER_MODEL
MIDDLEWARE = base.MIDDLEWARE
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
STATIC_ROOT = base.STATIC_ROOT


# Default primary key field type
DEFAULT_AUTO_FIELD = base.DEFAULT_AUTO_FIELD
