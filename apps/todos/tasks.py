from celery import shared_task
from django.utils import timezone
from .models import Todo
from apps.users.models import Notification


@shared_task
def send_reminders():
    now = timezone.now()
    for todo in Todo.objects.filter(reminder_date__lte=now):
        Notification.objects.create(
            user=todo.user,
            message=f"Reminder for your TODO: {todo.title}",
        )
