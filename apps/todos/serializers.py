from rest_framework import serializers
from apps.todos.models import Todo


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "title",
            "description",
            "due_date",
            "reminder_date",
            "created_at",
            "updated_at",
            "user",
        ]
        read_only_fields = ["created_at", "updated_at"]
