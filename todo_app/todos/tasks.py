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
            message=f'Reminder for your TODO: {reminder.todo.title}',
        )
        reminder.viewed = True
        reminder.count_not_viewed += 1
        reminder.save()

# @shared_task
# def send_reminders():
#     now = timezone.now()
#     reminders = Reminder.objects.filter(todo_item__due_date__lte=now, viewed=False)
#     for reminder in reminders:
#         send_mail(
#             'Reminder Notification',
        #     f'Reminder for your TODO item: {reminder.todo_item.title}',
        #     'heliavaliani@gmail.com',
        #     [reminder.todo_item.user.email],
        #     fail_silently=False,
        # )
        # reminder.viewed = True
        # reminder.save()
        #

# @shared_task
# def send_reminders():
#     now = timezone.now()
#     reminders = Reminder.objects.filter(todo_item__due_date__lte=now, viewed=False)
#     for reminder in reminders:
#         # Send email notification
#         send_mail(
        #     'Reminder Notification',
        #     f'Reminder for your TODO item: {reminder.todo_item.title}',
        #     'heliavaliani@gmail.com',
        #     [reminder.todo_item.user.email],
        #     fail_silently=False,
        # )
        # reminder.viewed = True
        # reminder.count_not_viewed += 1
        # reminder.save()
