"""
Django settings for hooslistening project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from pathlib import Path
import dj_database_url
import os

# Set to true if in development environment, else set to false if in production
DEVELOPMENT = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fl-b2ftmgk7&#h_$)7&-q7o4%$kwfz5t43kg3tu4l#clj@ckrl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hooslistening119.herokuapp.com', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'home.apps.HomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'social_app',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap4',
    'phone_field',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hooslistening.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hooslistening.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEVELOPMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = { #ACTUAL DATABASE FOR PRODUCTION
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd7o9bj1b2037v4',
            'USER': 'vsxtycthyvwfkv',
            'PASSWORD': 'e201fde8e0f1d989b2a7adff6a7a6d83b730213905bef4a5916e8691fcb05d67',
            'HOST': 'ec2-54-161-58-21.compute-1.amazonaws.com',
            'PORT': '5432',
            'TEST': {
                'NAME': 'd7o9bj1b2037v4',
            }
        }
    }
    d = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(d)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../home/static')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Stuff for Google Login
# https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5
AUTHENTICATION_BACKENDS = (
     'django.contrib.auth.backends.ModelBackend',
     'allauth.account.auth_backends.AuthenticationBackend',
 )

# SITE_ID = 3 For 127.0.0.1
# SIDE_ID = 4 For https://hooslistening119.herokuapp.com/
SITE_ID = 2

LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': '919486683843-7ekgvc6t9uod6rcqf603b1udglm8br4s.apps.googleusercontent.com',
            'secret': 'DIlanCzjvk4eGvS5TsuSB4Iq',
            'key': ''
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST = 'hooslistening.email'
EMAIL_HOST_USER = 'apikey'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_PASSWORD = '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'
EMAIL_HOST_PASSWORD = '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'


MEDIA_URL = '/documents/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'documents')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'hooslistening119f20'
AWS_S3_REGION_NAME = 'us-east-1'

AWS_ACCESS_KEY_ID = "AKIAY5DW2UKQHX5GTVYY"
AWS_SECRET_ACCESS_KEY = '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'

# Activate Django-Heroku.
try:
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False
