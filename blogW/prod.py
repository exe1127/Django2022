from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com','https://*.127.0.0.1','https://dev-blog-2022.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd35nbh5m8c38cn',
        'USER': 'ililqgqtiwkodc',
        'PASSWORD': 'e6017dfff8e3250fff9b3f26356a1d6c3c662008305df3e06b99f7d27383259e',
        'HOST': 'ec2-44-207-126-176.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}