"""
Django settings for agricom project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR,'reporter/static')
GDAL_LIBRARY_PATH = os.path.join(BASE_DIR,'GDAL/gdal304')
GEOS_LIBRARY_PATH = os.path.join(BASE_DIR,'GDAL/geos_c')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#16d&9$&ahec*jcsm3s_8g!==3c%t)ei_2xjzu0f4-_4bq^($3'
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'reporter.apps.ReporterConfig',
    'accounts.apps.AccountsConfig',
    'leaflet',
    'djgeojson',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agricom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'agricom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'railway',
        'USER': 'postgres',
        'HOST': 'containers-us-west-1.railway.app',
        'PASSWORD': 'pG7DrZxhTwLG6LCeFHkT',
        'PORT': '7058',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    STATIC_DIR,
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LEAFLET_CONFIG = {
    # Retirer 0.005 pour les 2 premières et ajouter 0.005 pour les 2 dernières
    'SPATIAL_EXTENT': (9.674, 4.014, 9.695, 4.034), # 4 corners
    'DEFAULT_CENTER': (9.683, 4.025), # lat,long
    'DEFAULT_ZOOM': 15,
    'MIN_ZOOM': 13,
    'TILES': [('Satellite','https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' ,
     {'attribution': '&copy; Big eye'}),
    ('Streets', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': '&copy; Contributors'})],
    # 'OVERLAYS': [('Cadastral', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': '&copy;IGN'})],
    'ATTRIBUTION_PREFIX': 'Powered by django-leaflet',
}
