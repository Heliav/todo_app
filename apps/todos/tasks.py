from celery import shared_task
from datetime import datetime
from .models import Todo
from apps.users.models import Notification


@shared_task
def send_reminders():
    now = datetime.now().replace(second=0, microsecond=0)
    for todo in Todo.objects.filter(reminder_date=now):
        Notification.objects.create(
            user=todo.user,
            message=f"Reminder for your TODO: {todo.title}",
        )


# print(f"{send_reminders=}")
