from pathlib import Path

from environ import Env
env = Env()
Env.read_env()


ENVIRONMENT = env('ENVIRONMENT', default='development')
# ENVIRONMENT = 'production'
DEV_ENVIRON = ENVIRONMENT == 'development'


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY', default='secret_key')

DEBUG = DEV_ENVIRON

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'docker-tutorial.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://docker-tutorial.up.railway.app']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'django_cleanup.apps.CleanupConfig',

    'django.contrib.sites',

    'django_celery_results',
    'django_celery_beat',

    'allauth',
    'allauth.account',

    'django_htmx',

    'a_home',
    'a_users',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'a_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'a_core.wsgi.application'


if DEV_ENVIRON:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'postgres',
            'PORT': 5432
        }
    }
    CELERY_BROKER_URL = 'redis://redis:6379/0'
else:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL', default='postgresql://'))
    }
    CELERY_BROKER_URL = env('REDIS_URL', default='redis://')


CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_EXTENDED = True


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_REDIRECT_URL = "{% url 'account_signup' %}?next={% url 'profile-onboarding' %}"


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
