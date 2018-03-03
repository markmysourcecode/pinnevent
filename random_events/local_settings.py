import os
from settings import SITE_ROOT, STATIC_DIR
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}'''

DEBUG = True
TEMPLATE_DEBUG = DEBUG
#ALLOWED_HOSTS = []
#STATICFILES_DIRS = [STATIC_DIR]

print('local settings is set')