import os
from . import base


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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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
MEDIA_URL = base.MEDIA_URL
STATICFILES_DIRS = base.STATICFILES_DIRS
STATIC_ROOT = base.STATIC_ROOT
MEDIA_ROOT = base.MEDIA_ROOT


# Default primary key field type
DEFAULT_AUTO_FIELD = base.DEFAULT_AUTO_FIELD
