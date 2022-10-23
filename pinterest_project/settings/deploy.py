from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-z*q$#la+z_+!t($td3@wej6%paxe##!zfz+xnrqjw9@bh)vk4j'
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER' : 'django',
        'PASSWORD' : 'password1234',
        'HOST' : 'mariadb',
        'PORT' : '3306',

    }
}