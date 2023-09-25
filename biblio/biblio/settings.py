"""
Django settings for biblio project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from configurations import Configuration

import os
from pathlib import Path
import hashlib
import uuid


def get_secret_key(base_dir='.'):
    def gen_key(key_path):
        with open(key_path, 'w') as key_file:
            key=hashlib.sha3_512(str(uuid.uuid4()).encode('utf8')).hexdigest()
            key_file.write(key)
        return key

    path = os.path.join(base_dir, '.secret.key')

    try:
        secret_key = open(path).read()
        assert secret_key, "Wrong secret key"
    except (IOError, AssertionError):
        secret_key = gen_key(path)
    return secret_key


BASE_DIR = Path(__file__).resolve().parent.parent


class Production(Configuration):
    
    # Build paths inside the project like this: BASE_DIR / 'subdir'.

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = get_secret_key(BASE_DIR)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = ['127.0.0.1']


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',      
        'bootstrap5',
        'crispy_forms',
        "crispy_bootstrap5",
        "rest_framework",

        ####
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',
        
        ###
        'shelf',
        'contact',
        'rental',
        'users',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        "allauth.account.middleware.AccountMiddleware",
    ]

    ROOT_URLCONF = 'biblio.urls'

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

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]

    WSGI_APPLICATION = 'biblio.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    AUTH_USER_MODEL = 'users.BiblioUser'


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    STATICFILES_DIRS = [
        ("media", MEDIA_ROOT),
        ]

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    LOGIN_REDIRECT_URL = 'main_page'
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = 'bootstrap5'

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }

class Dev(Production):
    DEBUG = True
    TEMPLATE_DEBUG = True
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

