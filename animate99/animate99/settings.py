"""
Django settings for animate99 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


from pathlib import Path
from decouple import config
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("DJANGO_SECRET_KEY", default='django-insecure-*4vwnjdg58b5*(e4!wn4d41+og2y^7pc8-uaat1c2o7v=ysyqf')
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'animate-99.herokuapp.com']


# Application definition

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    
    
    #3rd Party
    'django_extensions',
    'crispy_forms',
    'cloudinary',
    'cloudinary_storage',
    #apps
    'apps.common.apps.CommonConfig',
    'apps.main.apps.MainConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.user_review.apps.UserReviewConfig',
    'apps.blog.apps.BlogConfig',
    
    #google authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        
        'APP': {
            'client_id': '205496138072-9u3qvl2arbo61bcroogiuppr8kngsi26.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}


# Cloudinary configuration
cloudinary.config( 
  cloud_name = "dosj9cjie", 
  api_key = "177852858536987", 
  api_secret = "R8vSHpzBPvWvZ3k4fA4trIecaQg" 
)

# CLOUDINARY = {
#   'cloud_name' : "dosj9cjie", 
#   'api_key' : "177852858536987", 
#   'api_secret' : "R8vSHpzBPvWvZ3k4fA4trIecaQg" 
# }
ROOT_URLCONF = 'animate99.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
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

WSGI_APPLICATION = 'animate99.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
AUTH_USER_MODEL = "accounts.CustomUser"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles'), ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

WHITENOISE_USE_FINDERS = True
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#All_auth set up to remove user name field
SOCIALACCOUNT_FORMS ={'signup': 'apps.accounts.forms.CustomSignupForm'}
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'


MEDIA_URL = '/profilepics/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



# Account redirect URL

ACCOUNT_SIGNUP_REDIRECT_URL = "library"
LOGIN_REDIRECT_URL = "library"



SITE_ID = 1

SITE_ID = 1

#Email setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "animate99team99@gmail.com"
EMAIL_HOST_PASSWORD = "rrhwrsvquqznnahd"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
