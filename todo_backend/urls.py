from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import NotificationViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="todo app API",
        default_version="v1",
        description="API documentation for todo app system",
    ),
    public=True,
    permission_classes=[
        AllowAny,
    ],
)

router = DefaultRouter()
router.register(r"notifications", NotificationViewSet, basename="notification")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos/", include("apps.todos.urls")),
    path("users/", include("apps.users.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
