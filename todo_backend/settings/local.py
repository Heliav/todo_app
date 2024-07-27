from dotenv import load_dotenv

from .base import *
from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
load_dotenv()

os.environ["DEBUG"] = "true"

SECRET_KEY = str(os.getenv("SECRET_KEY"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_URL = "static/"

CELERY_BEAT_SCHEDULE = {
    "send-reminders": {
        "task": "todo_backend.tasks.send_reminders",
        "schedule": 60.0,
    },
}
