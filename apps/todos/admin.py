from django.contrib import admin
from apps.todos.models import Todo

admin.site.register(Todo)

# from celery.schedules import schedule
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Reminder
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
# import json
#
# class ReminderAdmin(admin.ModelAdmin):
#     list_display = ('todo_item', 'reminder_time', 'viewed')
#
#     admin.site.register(Reminder, UserAdmin)
#
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=1,
#         period=IntervalSchedule.DAYS,
# )
#
# # # Create a periodic task
# #     PeriodicTask.objects.create(
# #         interval=schedule,
# #         name='Send Reminder Emails',
# #         task='reminders.tasks.send_reminder_email',
# #         args=json.dumps([]),
# # )
