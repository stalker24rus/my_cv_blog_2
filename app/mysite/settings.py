import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_PATH = os.getenv('DJANGO_ENV_LOG_PATH')
WWW_ROOT = os.getenv('DJANGO_ENV_WWW_PATH')

SECRET_KEY = os.getenv('DJANGO_ENV_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('DJANGO_ENV_ALLOWED_HOSTS', 'localhost').split(',')

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',

    'blog.apps.BlogConfig',
    'cv.apps.CvConfig',

    'taggit',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432'
    }
}

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

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(WWW_ROOT, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(WWW_ROOT, 'media')

STATICFILES_DIRS = (
    os.path.join(WWW_ROOT, 'assets'),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_HOST = os.getenv('DJANGO_ENV_EMAIL_HOST')
EMAIL_PORT = os.getenv('DJANGO_ENV_EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('DJANGO_ENV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_ENV_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
# EMAIL_USE_SSL =
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/blog'
LOGIN_URL = '/blog/login'
LOGOUT_URL = '/blog/logout'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]
        ),
        'codeSnippet_theme': 'default',
    }

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic_formatter': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'main': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + 'main.log',
            'formatter': 'basic_formatter',
        },
        'cv': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + 'cv.log',
            'formatter': 'basic_formatter',
        },
        'blog': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + 'blog.log',
            'formatter': 'basic_formatter',
        },
    },
    'loggers': {
        '': {
            'handlers': ['main'],
            'level': 'INFO',
            'propagate': True,
        },
        'cv': {
            'handlers': ['cv'],
            'level': 'WARNING',
            'propagate': True,
        },
        'blog': {
            'handlers': ['blog'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
