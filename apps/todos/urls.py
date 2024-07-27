from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemListViewSet

router = DefaultRouter()
router.register(r"Todo", TodoItemListViewSet, basename="todo")

urlpatterns = [
    path("", include(router.urls)),
]
