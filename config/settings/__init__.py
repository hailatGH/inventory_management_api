import os
from datetime import timedelta

from dotenv import load_dotenv

from config.settings.base import *  # noqa: F403,F401

load_dotenv()

INSTALLED_APPS += [  # noqa: F405
    "rest_framework",
    "rest_framework_simplejwt",
    "user",
    "warehouse",
    "product",
    "sale",
]

AUTH_USER_MODEL = "user.Users"

# Simple JWT conf
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=60),
}

STATIC_URL = "static/"
STATIC_ROOT = "static/"

MEDIA_URL = "media/"
MEDIA_ROOT = "media/"

# Import setting based on debug val
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
if not DEBUG:
    from config.settings.dev import *  # noqa: F403,F401
else:
    from config.settings.prod import *  # noqa: F403,F401
