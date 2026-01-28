
import os
from pathlib import Path
import platform

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*&nu_v#s362hoz_nw!u%9^tx!oq19rp9p87aposdn(1za!g)kc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.login_required.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'Exportaciones.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Exportaciones.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'exportaciones',
        'USER': 'postgres',
        'PASSWORD': 'hnl49sec',
        'HOST': 'localhost',  # o IP de tu servidor PostgreSQL
        'PORT': '5432',       # puerto por defecto
    },
    'catastro':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CatastroMineroSalta',
        'USER': 'postgres',
        'PASSWORD': 'veldspar',
        'HOST': '192.168.0.4',  # o IP de tu servidor PostgreSQL
        'PORT': '5432',  
    },
    'simsa':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simsadb',
        'USER': 'postgres',
        'PASSWORD': '14Gp4sLKZyTL8KG',
        'HOST': '172.17.1.239',
        'PORT': '5432',
    }
    #DB_NAME=CatastroMineroSalta
#DB_USER=postgres
#DB_PASSWORD=veldspar
#DB_HOST=192.168.0.4
#DB_PORT=5432
}

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = '/login/'  # Asegúrate de que esta URL exista

# Ruta absoluta donde Django buscará archivos estáticos si hacés collectstatic
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),  # Para una carpeta global opcional
#]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Expira la sesión después de X segundos de inactividad
SESSION_COOKIE_AGE = 3600  # 30 minutos (en segundos)

# Restablece el temporizador de expiración con cada solicitud
SESSION_SAVE_EVERY_REQUEST = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'secretariademineriadesalta@gmail.com'
EMAIL_HOST_PASSWORD = 'coja wtju azwh kaxv'  # Contraseña de aplicación (segura)

#EMAIL_HOST_USER = "mesadeayudasimsa@gmail.com"
#EMAIL_HOST_PASSWORD = "rkfw qytu qntg auua"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
STATIC_ROOT = BASE_DIR / 'staticfiles'
SITE_URL = "http://192.168.0.233/home"
ORGANISMO = "Secretaría de Minería y Energía"

# Si estás en Windows (Desarrollo)
if platform.system() == 'Windows':
    MEDIA_ROOT = 'Z:/media/' 
# Si estás en Linux (Servidor Real)
else:
    MEDIA_ROOT = '/mnt/servidor_nas/media/'

MEDIA_URL = '/media/'