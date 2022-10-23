from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-z*q$#la+z_+!t($td3@wej6%paxe##!zfz+xnrqjw9@bh)vk4j'
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}