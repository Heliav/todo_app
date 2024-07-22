import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_app.settings")

app = Celery("todo_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    "send-reminders-every-minute": {
        "task": "todos.tasks.send_reminders",
        "schedule": 60.0,  # Every 60 seconds
    },
}
