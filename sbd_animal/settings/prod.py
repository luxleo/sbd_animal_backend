import os
from .common import *

SECURE_CROSS_ORIGIN_OPENER_POLICY = False
DEBUG = False
ALLOWED_HOSTS = ["52.79.170.98", "sbd-animal.com", "sbd-animal.vercel.app"]
# csrf and session token config
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CORS_ALLOWED_ORIGINS = [
    "http://sbd-animal.com",
    "https://sbd-animal.com",
    "http://52.79.170.98",
    "https://52.79.170.98",
    "https://sbd-animal.vercel.app",
]
# DATABASE config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "dbmaster",
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": "3306",
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=1),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # custom field
    "AUTH_COOKIE_ACCESS": "access_token",  # Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_REFRESH": "refresh_token",
    "AUTH_COOKIE_DOMAIN": "/",  # A string like "example.com", or None for standard domain cookie.
    "AUTH_COOKIE_SECURE": True,  # Whether the auth cookies should be secure (https:// only).
    "AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag.It's not fetch by javascript.
    "AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
    "AUTH_COOKIE_SAMESITE": "None",
}

# NOTE: celery settings
CELERY_TIMEZONE = "Asia/Seoul"
CELERY_BROKER_URL = "redis://sbd_redis:6379"
CELERY_RESULT_BACKEND = "redis://sbd_redis:6379"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# SMTP settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Storage config
DEFAULT_FILE_STORAGE = "sbd_animal.storages.MediaStorage"  # upload media file
STATICFILES_STORAGE = "sbd_animal.storages.StaticStorage"  # hold static files
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False
