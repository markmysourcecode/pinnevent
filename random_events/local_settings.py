import os
from settings import SITE_ROOT
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

print(SITE_ROOT)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG
STATICFILES_DIRS = os.path.join(SITE_ROOT, 'static')

print('local settings')