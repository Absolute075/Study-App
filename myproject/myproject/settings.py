
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Quick-start development settings - unsuitable for production
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
    'logs.apps.LogsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'accounts.middleware.BlockedUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.mymiddleware.MyMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # имя базы в Supabase
        'USER': 'postgres.cozecdjfnbhdndcivcvs',  # пользователь базы
        'PASSWORD': 'star4536446',  # пароль пользователя
        'HOST': 'aws-1-eu-central-1.pooler.supabase.com',  # Pooler host
        'PORT': '6543',  # Pooler port
    }
}




# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings
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
            "permissions": ["is_superuser"],
        },
    ],
    "order_with_respect_to": ["auth", "courses", "grades"],
    "theme": "flatly",
    "custom_links": {
        "auth": [
            {"name": "Добавить студента", "url": "/admin/auth/user/add/", "icon": "fas fa-user-plus"},
            {"name": "Добавить группу", "url": "/admin/auth/group/add/", "icon": "fas fa-plus-circle"},
        ]
    },
}

LOGIN_REDIRECT_URL = '/admin/'

