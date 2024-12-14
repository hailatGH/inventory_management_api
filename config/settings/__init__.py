import os

from dotenv import load_dotenv

from config.settings.base import *  # noqa: F403,F401

load_dotenv()

INSTALLED_APPS += ["user", "rest_framework"]  # noqa: F405
AUTH_USER_MODEL = "user.Users"

# Import setting based on debug val
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
if not DEBUG:
    from config.settings.dev import *  # noqa: F403,F401
else:
    from config.settings.prod import *  # noqa: F403,F401
