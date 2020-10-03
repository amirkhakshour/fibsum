"""Default configuration

Use env var to override
"""
import os
import distutils.util
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
READ_DOT_ENV_FILE = distutils.util.strtobool(os.getenv("READ_DOT_ENV_FILE", default="False"))
if READ_DOT_ENV_FILE:
    from dotenv import load_dotenv   # NOQA
    load_dotenv()
    env_path = BASE_DIR / '.env'
    load_dotenv(dotenv_path=env_path)

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

# health check config
HEALTH_SUCCESS_TTL = os.getenv("HEALTH_SUCCESS_TTL", default=30)
HEALTH_FAILED_TTL = os.getenv("HEALTH_FAILED_TTL", default=10)
