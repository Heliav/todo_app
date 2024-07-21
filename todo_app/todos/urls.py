from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemListViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'Todo', TodoItemListViewSet, basename='todo')
router.register(r'Reminder', ReminderViewSet, basename='reminder')

urlpatterns = [
    path('', include(router.urls)),
]
