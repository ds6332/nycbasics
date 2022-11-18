"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
import environ

env = environ.Env()
environ.Env.read_env()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*s62_zi-k=3ys38hfsh4zi4d(ctav0f6uig7p^mjh7bx5+aq-o"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "nycbasics5.ga",
    "NYCbasics-staging.eba-itqvcpc2.us-west-2.elasticbeanstalk.com",
    "NYCbasics-prod.eba-itqvcpc2.us-west-2.elasticbeanstalk.com",
    "nycbasics5prod.ml",
    "localhost",
    "nycstaging-env.eba-6p2tbyi2.us-west-2.elasticbeanstalk.com",
    "nycprod-env.eba-6p2tbyi2.us-west-2.elasticbeanstalk.com",
    "nycbasics-prod-env.eba-s8mf4mpn.us-west-2.elasticbeanstalk.com",
    "nycbasics-staging-env.eba-gvsq4xxk.us-west-2.elasticbeanstalk.com",
]
# add aws cname here after green eb status

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    # Registering the NycBasics Application
    "NycBasics.apps.NycbasicsConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "backend.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "frontend/build"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),
    }
}
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("dbname"),
        "USER": config("dbuser"),
        "PASSWORD": config("dbpassword"),
        "HOST": config("dbhost"),
        "PORT": config("dbport"),
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# /home/suyash/team-5-inperson/backend/NycBasics/static
# STATIC_ROOT = '/home/suyash/team-5-inperson/backend/backend/static'
# '/home/django/django_project/django_project/static'
STATIC_ROOT = os.path.join(BASE_DIR, "frontend/build/static/")

STATIC_URL = "static/"
"""
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static'),
]
"""
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://NYCbasics-staging.eba-itqvcpc2.us-west-2.elasticbeanstalk.com",
    "http://nycbasics5.ga",
    "https://nycbasics5.ga",
    "https://NYCbasics-staging.eba-itqvcpc2.us-west-2.elasticbeanstalk.com",
    "http://NYCbasics-prod.eba-itqvcpc2.us-west-2.elasticbeanstalk.com",
    "https://NYCbasics-prod.eba-itqvcpc2.us-west-2.elasticbeanstalk.com",
    "http://nycbasics5prod.ml",
    "https://nycbasics5prod.ml",
    "http://nycstaging-env.eba-6p2tbyi2.us-west-2.elasticbeanstalk.com",
    "https://nycstaging-env.eba-6p2tbyi2.us-west-2.elasticbeanstalk.com",
    "http://nycprod-env.eba-6p2tbyi2.us-west-2.elasticbeanstalk.com",
    "https://nycprod-env.eba-6p2tbyi2.us-west-2.elasticbeanstalk.com",
    "http://nycbasics-prod-env.eba-s8mf4mpn.us-west-2.elasticbeanstalk.com",
    "http://nycbasics-staging-env.eba-gvsq4xxk.us-west-2.elasticbeanstalk.com",
]
# may need to add aws eb cname here above
