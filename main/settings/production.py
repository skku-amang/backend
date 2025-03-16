import os
from . import base


BASE_DIR = base.BASE_DIR
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

# Application definition
INSTALLED_APPS = base.INSTALLED_APPS + [
    "storages",
    "corsheaders",
]
AUTH_USER_MODEL = base.AUTH_USER_MODEL
MIDDLEWARE = base.MIDDLEWARE
ROOT_URLCONF = base.ROOT_URLCONF
TEMPLATES = base.TEMPLATES
WSGI_APPLICATION = base.WSGI_APPLICATION
REST_FRAMEWORK = base.REST_FRAMEWORK
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
]


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


# AWS S3
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "mediafiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"

# MinIO 설정
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_STATIC_BUCKET_NAME = os.environ.get("AWS_STATIC_BUCKET_NAME")
AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL")
AWS_S3_REGION_NAME = os.environ.get(
    "AWS_S3_REGION_NAME"
)  # 미니오는 지역을 무시하지만 필요함

# S3 옵션
AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_FILE_OVERWRITE = False

# 미디어와 스태틱 URL 설정
STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STATIC_BUCKET_NAME}/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/"


# CORS
CORS_ALLOWED_ORIGINS = os.environ.get("DJANGO_CORS_ALLOWED_ORIGINS").split(",")
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
