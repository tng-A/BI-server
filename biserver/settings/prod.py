"""
Production settings.
"""

import os

from .base import *

DEBUG = os.environ.get('DEBUG', '').lower() == 'true'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.herokuapp.com'
]

INSTALLED_APPS += 'corsheaders'

MIDDLEWARE += 'corsheaders.middleware.CorsMiddleware'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    '*'
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '')
CORS_ORIGIN_ALLOW_ALL = os.environ.get('CORS_ORIGIN_ALLOW_ALL', True)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
