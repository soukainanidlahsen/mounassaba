"""
Mounassaba — Production settings.
Requires PostgreSQL and proper environment configuration.
"""
from .base import *  # noqa: F401, F403

from decouple import config

# =============================================================================
# Database — PostgreSQL for production
# =============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='mounassaba'),
        'USER': config('DB_USER', default='mounassaba'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# =============================================================================
# Security
# =============================================================================
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
