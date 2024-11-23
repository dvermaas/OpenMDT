import os
from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Application definition

INSTALLED_APPS = [
    "accounts.apps.AccountsConfig",
    "common.apps.CommonConfig",
    "reports.apps.ReportConfig",
    "profiles.apps.ProfilesConfig",
    "legislations.apps.LegislationsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "silk",
    "simple_history",
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "DjangoPolls.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [BASE_DIR / "templates"],
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "common.context_processors.notifications",
            ],
        },
    },
]

WSGI_APPLICATION = "DjangoPolls.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "accounts.User"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "templates/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Debug toolbar
if env.bool(" DEBUG_TOOLBAR", False):
    INTERNAL_IPS = ["127.0.0.1"]

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# Django Silk
SILKY_AUTHORISATION = True
SILKY_META = True
SILKY_MAX_RECORDED_REQUESTS = 10 ** 4

# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "uploads"

# Client Cache
USE_ETAGS = True

# Cache
if env.bool("USE_CACHE", False):
    REDIS_HOST = env.str("REDIS_HOST")
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f"redis://{REDIS_HOST}:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
    CACHE_TIMEOUT = 60 * 60 * 24 * 7

# Storage
if env.bool("USE_S3", False):
    AWS_S3_ACCESS_KEY_ID = env.str("AWS_S3_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY = env.str("AWS_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = env.str("AWS_S3_ENDPOINT_URL")
    AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", None)
    AWS_S3_SIGNATURE_VERSION = env.str("AWS_S3_SIGNATURE_VERSION", "s3v4")
    AWS_S3_VERIFY = env.str("AWS_S3_VERIFY", False)
    AWS_S3_USE_SSL = env.str("AWS_S3_VERIFY", True)
    AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", "us-east-1")
    if AWS_S3_CUSTOM_DOMAIN and DEBUG:
        AWS_S3_URL_PROTOCOL = "http:"
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "location": "media",
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "signature_version": "s3v4",
                "use_ssl": True,
                "client_config": None,
            },
        },
    }

# allauth

SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'FIELDS': ['id', 'email', 'first_name', 'last_name', 'profile_image'],
    }
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "stream": sys.stdout,  # Log to stdout
#             "formatter": "verbose",  # Choose your desired formatter
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": os.getenv(
#                 "DJANGO_LOG_LEVEL", "DEBUG"
#             ),  # Set log level through environment variable
#             "propagate": True,
#         },
#         "boto3": {
#             "handlers": ["console"],
#             "level": os.getenv("DJANGO_LOG_LEVEL", "DEBUG"),
#             "propagate": True,
#         },
#         "botocore": {
#             "handlers": ["console"],
#             "level": os.getenv("DJANGO_LOG_LEVEL", "DEBUG"),
#             "propagate": True,
#         },
#     },
# }
