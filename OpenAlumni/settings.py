"""
Django settings for OpenAlumni project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

from OpenAlumni.passwords import DB_PASSWORD

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL_TESTER = ["hhoareau@gmail.com",
                "paul.dudule@gmail.com",
                "roger.legumes@gmail.com",
                "j.lecanu@femis.fr",
                "rv@f80.fr",
                "herve.hoareau@f80.fr",
                "sophie.dudule@gmail.com"]

LOCAL_FEDORA_SERVER='172.23.80.132'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')0p@7b_kew8_w+jjuv=(zbn!sp!bm2*=7$s7#%@bvkwy0i--0p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [
    "*",
    "*.github.com",
    "server.f80.fr",
    "localhost",
    "127.0.0.1",
    "dcp.f80.fr"
]



STATIC_URL  = "/static/"
STATIC_ROOT=os.path.join(BASE_DIR, "static")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'dbbackup',
    'oauth2_provider',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'sslserver',
    'alumni.apps.AlumniConfig',
    'django_elasticsearch_dsl',
    'django_filters',
    'django_elasticsearch_dsl_drf',
    'django.contrib.staticfiles',
    'graphene_django'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/static/'}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['http://localhost:4200']

ROOT_URLCONF = 'OpenAlumni.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OpenAlumni.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# "prod": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "alumni_db",
#         "USER": "hhoareau",
#         "PASSWORD": "hh4271",
#         'HOST': '161.97.75.165',
#         'PORT': '5432',
#         'OPTIONS': {
#             'options': '-c statement_timeout=5000'
#         }
#     },
# "dev": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "alumni_db",
#         "USER": "hhoareau",
#         "PASSWORD": "hh4271",
#         'HOST': '207.180.198.227',
#         'PORT': '5432',
#         'OPTIONS': {
#             'options': '-c statement_timeout=5000'
#         }
#     }
# 'sqllite': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': os.path.join(BASE_DIR, 'alumni_db'),
# },

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "alumni_db",
        "USER": "hhoareau",
        "PASSWORD": DB_PASSWORD,
        'HOST': '161.97.75.165',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c statement_timeout=5000'
        }
    },

    "dev": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "alumni_db",
            "USER": "hhoareau",
            "PASSWORD": DB_PASSWORD,
            'HOST': LOCAL_FEDORA_SERVER,
            'PORT': '5432',
            'OPTIONS': {
                'options': '-c statement_timeout=5000'
            }
        }
}

#Installation d'
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': '161.97.75.165:9200'
    },
    'dev': {
        'hosts': LOCAL_FEDORA_SERVER+':9200'
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 500,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'ORDERING_PARAM':'ordering',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


GRAPHENE = {
    'SCHEMA': 'alumni.profil.schema'
}



#https://django-elasticsearch-dsl-drf.readthedocs.io/en/latest/quick_start.html#installation
#chemin du répertoire document



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


EMAIL_HOST ="smtp.ionos.fr"
EMAIL_PORT = 587
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST_USER ="reply@f80.fr"
EMAIL_HOST_PASSWORD ="Hh42714280"

APPNAME="Data Culture Pro"

#DOMAIN_APPLI="http://localhost:4200"
#DOMAIN_SERVER="http://localhost:8000"
DOMAIN_APPLI="https://dcp.f80.fr"
DOMAIN_SERVER="https://server.f80.fr:8000"


LINKEDIN_API_KEY="86sko2r66j8l8k"
LINKEDIN_API_SECRET="5daYMxKMEvWvfiuX"
LINKEDIN_RETURN_URL="http://localhost:8000/api/oauth_callback"


#Sécurisation
#SECURE_SSL_REDIRECT = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MOVIE_CATEGORIES=[
"Documentary","Action","Adventure","Sci-Fi","Mystery","Horror","Thriller","Animation","Comedy","Family","Fantasy","Drama","Music","Biography","Romance","History","Crime","Western","War","Musical","Sport"
]
MOVIE_NATURE=["Serie","TV","Short","Long","Documentary"]