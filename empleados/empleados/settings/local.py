
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    ]}
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('DB_NAME'),
        'HOST': 'localhost',
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

# La URL donde se accedera a buscar la imagenes 
MEDIA_URL = '/media/' #los archivos estaticos
MEDIA_ROOT = BASE_DIR.child('media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mvmoii29@gmail.com'
EMAIL_HOST_PASSWORD = 'racnarocc00260'
EMAIL_USE_TLS = True