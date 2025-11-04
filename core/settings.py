import os
from pathlib import Path
import cloudinary_storage
import dj_database_url
from cloudinary_storage.storage import MediaCloudinaryStorage

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

# FORCE CLOUDINARY STORAGE - ADD THESE LINES
import django.core.files.storage
django.core.files.storage.default_storage = cloudinary_storage.storage.MediaCloudinaryStorage()

# Media files - ENABLE CLOUDINARY
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s4(+!_@%$4$_f*(9-@yz8q_x!jo0vj0r(2!79ja&wmib1t8ek%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
    'contact',
    'blog',
    'markdownx',
    "cloudinary",
    "cloudinary_storage",
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fiksengineer@gmail.com'
EMAIL_HOST_PASSWORD = '@gp200.com'

# Database
DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://fiks:npg_hiolXr7MF8Ix@ep-polished-mode-agafl9xc-pooler.c-2.eu-central-1.aws.neon.tech/profile?sslmode=require&channel_binding=require",
        conn_max_age=600
    )
}

STATIC_ROOT = BASE_DIR / "staticfiles"

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cloudinary media URL (remove local media settings)
MEDIA_URL = '/media/'  # This is fine for URL generation, but files go to Cloudinary
# REMOVED: MEDIA_ROOT = os.path.join(BASE_DIR, 'media') - This conflicts with Cloudinary