#https://www.youtube.com/watch?v=RsiXzwesNLQ&list=PLPNDH2COtd60EX8roZCeIddkimMhBlTrX&index=6
##https://youtu.be/lKyH_ZGtvwM
#https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
#partly based on youtube tutorial and partly based on perplxewity answers and based on django storage amazon s3 documentation

"""
Django settings for learnimageupload project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import environ
from decouple import config

from pathlib import Path


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$70+gt3jt1luskn50vkq48c2=cgfm1hlb=jj93v6n^9ed$=!@7'

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
    'imageuploadapp',
    'widget_tweaks',
    'django_extensions',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learnimageupload.urls'

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

WSGI_APPLICATION = 'learnimageupload.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT= BASE_DIR / 'media'
MEDIA_URL = '/media/'

#DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
#DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"



'''AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')   

AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
#AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')'''

AWS_S3_CUSTOM_DOMAIN=config('AWS_S3_CUSTOM_DOMAIN')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
AWS_CLOUDFRONT_KEY=env.str('AWS_CLOUDFRONT_KEY',multiline=True).encode('ascii').strip()
AWS_CLOUDFRONT_KEY_ID=env.str('AWS_CLOUDFRONT_KEY_ID').strip()
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
          "access_key": AWS_ACCESS_KEY_ID,
          "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_S3_REGION_NAME,
             "custom_domain": AWS_S3_CUSTOM_DOMAIN,
             "cloudfront_key": AWS_CLOUDFRONT_KEY,
            "cloudfront_key_id": AWS_CLOUDFRONT_KEY_ID,
            "querystring_expire":20 # Query string expiration time(uploaded image will be available for 20 seconds),
            
        },
    },
    
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,  # Corrected here
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_S3_REGION_NAME,
            "custom_domain": AWS_S3_CUSTOM_DOMAIN,
            "cloudfront_key": AWS_CLOUDFRONT_KEY,
            "cloudfront_key_id": AWS_CLOUDFRONT_KEY_ID,
            "location": 'static',  # Path within the bucket for static files
            "default_acl": 'public-read',  # ACL for static files
            "querystring_expire":20   # Query string expiration time(uploaded image will be available for 20 seconds)
        },
    },
}

