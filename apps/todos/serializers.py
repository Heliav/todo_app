from rest_framework import serializers
from apps.todos.models import Todo


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
