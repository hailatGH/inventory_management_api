import os

from dotenv import load_dotenv

from config.settings.base import *  # noqa: F403,F401

load_dotenv()

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

if not DEBUG:
    from config.settings.dev import *  # noqa: F403,F401
else:
    from config.settings.prod import *  # noqa: F403,F401
