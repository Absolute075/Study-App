from typing import Any
from pathlib import Path
import os

BASE_DIR: Any = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



SECRET_KEY = 'django-insecure-zmh04bp-a+fxk%jnd-kg@5kwn=tc)8wwc%pk25cqxjd@sc5_o8'

DEBUG = True

ALLOWED_HOSTS = ['study-app-a53x.onrender.com']






# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'accounts',
    'logs',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'accounts.middleware.BlockedUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # твой middleware
    'middleware.mymiddleware.MyMiddleware',
]



ROOT_URLCONF = 'myproject.urls'



from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

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





JAZZMIN_SETTINGS = {
    "site_title": "Учебная панель ProLearner",
    "site_header": "Панель администратора ProLearner",
    "site_brand": "ProLearner",
    "welcome_sign": "Добро пожаловать в панель администратора ProLearner!",
    "site_footer": "© 2025 ProLearner — Все права защищены",

    "search_model": ["auth.User", "auth.Group"],

    "icons": {
        "auth": "fas fa-users",
        "auth.user": "fas fa-user-graduate",
        "auth.group": "fas fa-chalkboard-teacher",
    },

    "menu": [
    {"model": "admin.logentry", "name": "Логи действий (Системные)", "icon": "fas fa-history"},
    {"model": "logs.actionlog", "name": "Логи действий (Пользовательские)", "icon": "fas fa-clipboard-list"},
    {
        "name": "Дашборд",
        "url": "/admin/dashboard/",
        "icon": "fas fa-chart-bar",
        "permissions": ["is_superuser"],  # Добавляем, чтобы видели только админы
    },
],


    "order_with_respect_to": ["auth", "courses", "grades"],

    "theme": "flatly",

    "custom_links": {
        "auth": [
            {
                "name": "Добавить студента",
                "url": "/admin/auth/user/add/",
                "icon": "fas fa-user-plus",
            },
            {
                "name": "Добавить группу",
                "url": "/admin/auth/group/add/",
                "icon": "fas fa-plus-circle",
            },
        ]
    },
}



LOGIN_REDIRECT_URL = '/admin/'



WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
