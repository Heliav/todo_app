from celery import shared_task
from django.utils import timezone
from .models import Reminder
from todo_app.users.models import Notification


@shared_task
def send_reminders():
    now = timezone.now()
    reminders = Reminder.objects.filter(todo__due_date__lte=now, viewed=False)
    for reminder in reminders:
        Notification.objects.create(
            user=reminder.todo.user,
            message=f"Reminder for your TODO: {reminder.todo.title}",
        )
        reminder.viewed = True
        reminder.count_not_viewed += 1
        reminder.save()
