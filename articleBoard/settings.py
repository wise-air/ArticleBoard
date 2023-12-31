"""
Django settings for articleBoard project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import path

from secret import EMAIL_FOR_SEND, EMAIL_FOR_SEND_PASS, KEY_FOR_IFRAME

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u3co4i3(g2*s%2&ts$o^x3t45i7%x5&@s3akdu*qj2sbjvuyqg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'board',
    'ckeditor',
    'ckeditor_uploader',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'articleBoard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'articleBoard.wsgi.application'


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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATH = [
    path.join(BASE_DIR, 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
PROJECT_PATH = path.abspath(path.dirname(__name__))
SITE_ROOT = path.dirname(path.realpath(__file__))
# STATIC_ROOT = path.join(PROJECT_PATH, "static")
MEDIA_ROOT = path.join(PROJECT_PATH, "media")


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor

# CKEDITOR_BASEPATH = path.join(STATIC_ROOT, 'ckeditor/ckeditor/')
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = True


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'removeButtons': ','.join([
            'Save',
            'NewPage',
            'ExportPdf',
            'Preview',
            'Print',
            'Scayt',
            'Form',
            'Checkbox',
            'Radio',
            'TextField',
            'Textarea',
            'Select',
            'Button',
            'HiddenField',
            'Language',
            'Flash',
            'PageBreak',
            'CreateDiv',
            'EmbedSemantic',
        ]),
        'extraPlugins': ','.join([
            'autoembed',
            'embed',
            'filebrowser',
            'image2',
            'uploadimage',
            'div',
            'autolink',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'embed_provider': f'//iframe.ly/api/oembed?url={{url}}&callback={{callback}}&api_key={KEY_FOR_IFRAME}',
    }
}


# e-mail for sending
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = EMAIL_FOR_SEND
EMAIL_HOST_PASSWORD = EMAIL_FOR_SEND_PASS
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'wisears@yandex.ru'

# Celery

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Yekaterinburg'


# allauth

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/board/ad'
LOGOUT_REDIRECT_URL = '/board/ad'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_DISPLAY = 'board.models.return_user_email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/board/ad'
