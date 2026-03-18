"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# SECURITY（满分版）
# ========================

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-dev-key")

# 🚀 自动判断环境（关键）
DEBUG = os.environ.get("RENDER") is None

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com"
]


# ========================
# APPLICATIONS
# ========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # project apps
    'items',
    'comments',
    'users',
    'cart',

    # cloudinary
    'cloudinary',
    'cloudinary_storage',
]


# ========================
# MIDDLEWARE
# ========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ⭐ 必须在前
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================
# URL / TEMPLATES
# ========================

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_count',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'


# ========================
# DATABASE（Render兼容）
# ========================

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ========================
# PASSWORD VALIDATION
# ========================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ========================
# INTERNATIONALIZATION
# ========================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ========================
# STATIC FILES（满分关键）
# ========================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ========================
# MEDIA FILES
# ========================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ========================
# CLOUDINARY（自动切换）
# ========================

if os.environ.get("CLOUDINARY_URL"):
    # Render 自动使用环境变量
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    # 本地开发
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'dyeszxa9y',
        'API_KEY': '413121915428448',
        'API_SECRET': 'dj1AYh7XcfNgmMEi19OhvsXGNj8',
    }


# ========================
# AUTH REDIRECT
# ========================

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# ========================
# DEFAULT FIELD
# ========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'