import os
from . import base


BASE_DIR = base.BASE_DIR
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = os.environ.get("DJANGO_DEBUG", False)
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
API_KEY = os.environ.get("DJANGO_API_KEY")

# Application definition
INSTALLED_APPS = base.INSTALLED_APPS + [
    "storages",
    "corsheaders",
    "rest_framework_api_key",
]
AUTH_USER_MODEL = base.AUTH_USER_MODEL
MIDDLEWARE = base.MIDDLEWARE + [
    "corsheaders.middleware.CorsMiddleware",
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


# Password validation
AUTH_PASSWORD_VALIDATORS = base.AUTH_PASSWORD_VALIDATORS


# JWT
SIMPLE_JWT = base.SIMPLE_JWT


# Internationalization
LANGUAGE_CODE = base.LANGUAGE_CODE
TIME_ZONE = base.TIME_ZONE
USE_I18N = base.USE_I18N
USE_TZ = base.USE_TZ


# AWS S3
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "mediafiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}
AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.environ.get("AWS_SESSION_TOKEN")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + f".s3.{AWS_REGION}.amazonaws.com"
AWS_QUERYSTRING_AUTH = False


# Static files (CSS, JavaScript, Images)
STATIC_URL = base.STATIC_URL
MEDIA_URL = base.MEDIA_URL
STATICFILES_DIRS = base.STATICFILES_DIRS
STATIC_ROOT = base.STATIC_ROOT
MEDIA_ROOT = base.MEDIA_ROOT

# CORS_ALLOWED_ORIGINS = os.environ.get("DJANGO_CORS_ALLOWED_ORIGINS").split(",")
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ["*"]

# Default primary key field type
DEFAULT_AUTO_FIELD = base.DEFAULT_AUTO_FIELD


# Default Login
LOGIN_REDIRECT_URL = base.LOGIN_REDIRECT_URL
LOGOUT_REDIRECT_URL = base.LOGOUT_REDIRECT_URL
