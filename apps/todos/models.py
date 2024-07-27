from datetime import timedelta
from django.utils import timezone
from django.db import models
from apps.users.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default="description")
    due_date = models.DateTimeField()
    reminder_date = models.DateTimeField(default=timezone.now() + timedelta(days=-1))
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if not self.reminder_time:
    #         self.reminder_time = self.due_date - timedelta(days=1)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title
