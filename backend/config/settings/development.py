"""
Mounassaba — Development settings.
Uses SQLite by default for zero-configuration setup.
"""
from .base import *  # noqa: F401, F403

# =============================================================================
# Database — SQLite for development
# =============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =============================================================================
# Debug
# =============================================================================
DEBUG = True

# =============================================================================
# Email — Console backend for development
# =============================================================================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
