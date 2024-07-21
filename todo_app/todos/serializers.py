from rest_framework import serializers
from todo_app.todos.models import Todo, Reminder
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
