from django.db import models
from ..users.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default="description")
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Reminder(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.todo.title} at {self.reminder_date}"
