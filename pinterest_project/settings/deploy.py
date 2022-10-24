from http import server
from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()

    return secret

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER' : 'django',
        'PASSWORD' : read_secret('MYSQL_PASSWORD'),
        'HOST' : 'mariadb',
        'PORT' : '3306',

    }
}