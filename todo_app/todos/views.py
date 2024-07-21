from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import TodoItemSerializer, ReminderSerializer
from ..todos.models import Todo, Reminder


class ReminderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(todo__user=self.request.user)


class TodoItemListViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
