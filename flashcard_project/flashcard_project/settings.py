import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Assuming BASE_DIR is defined

STATIC_URL = '/static/'
STATICFILES_DIRS = ['/Users/bengalurubabu/PycharmProjects/Language_Learning_Flashcards_App/flashcard_project/static']  # For additional static files during development
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Where collectstatic will gather static files for production

# Set your secret key (ensure this is kept secret!)
SECRET_KEY = 'your-very-secret-key-goes-here'

# settings.py
DEBUG = True
# settings.py
'''DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']'''
ROOT_URLCONF = 'flashcard_project.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # other apps
    # linking flashcards app to project(flashcard_project/settings.py)
    'flashcards',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Place this first
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # This should come after SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
