"""
Django settings for zt project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url


DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        default='postgres://localhost/zavod')}

ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',')]
#SECRET_KEY = os.getenv('SECRET_KEY', 't(nfnhm*u5d*lgg^n60go(h6je)133c3j*a3c@)7cp8v+e7@)a')
#STATIC_ROOT = os.getenv('STATIC_ROOT')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w1dctza7jsot5d6ba(h))qvg5c@q=hrq@ik_2h-9tp9hpbe0*t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'watson',
    'threadedcomments',
    'django_comments',
    'django.contrib.sites',
    'social.apps.django_app.default',
    # 'fluent_contents.plugins.text',
    'django_wysiwyg',
    'ckeditor',
    'zavod',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'assets', 'static', 'build'),
            os.path.join(BASE_DIR, 'zavod', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'zavod.context_processors.news_for_bottom',
                'zavod.context_processors.product_for_bottom',
                'zavod.context_processors.media_for_bottom',
                'zavod.context_processors.black_friday_product',
                'zavod.context_processors.callme_form',
                'zavod.context_processors.log_in_form',
                'zavod.context_processors.registration_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'zt.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets', 'static', 'build')]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'assets', 'media')
MEDIA_URL = '/media/'

# Auth settings

AUTH_USER_MODEL = 'zavod.CustomUser'

SOCIAL_AUTH_USER_MODEL = 'zavod.CustomUser'

AUTHENTICATION_BACKENDS = (
    'social.backends.vk.VKOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_VK_OAUTH2_KEY = ''
SOCIAL_AUTH_VK_OAUTH2_SECRET = ''

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_VK_OAUTH2_SCOPE = [
  'notify',
  'email',
]

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

# Comments

COMMENTS_APP = 'threadedcomments'

SITE_ID = 1

# Email

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EMAILS_FOR_FAQ = ['']
EMAILS_FOR_CALLBACK = ['']

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_app.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# ckeditor settings

CKEDITOR_UPLOAD_PATH = os.path.join('media/', 'images')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

# Local settings

try:
    from zt.local_settings import *
except ImportError:
    pass