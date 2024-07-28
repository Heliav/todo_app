import datetime
from datetime import timedelta
from django.db import models
from apps.users.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default="description")
    due_date = models.DateTimeField()
    reminder_date = models.DateTimeField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.reminder_date:
            self.reminder_date = self.reminder_date.replace(second=0, microsecond=0)
        else:
            self.reminder_date = datetime.datetime.now().replace(
                second=0, microsecond=0
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
