from django.contrib.auth import login
from rest_framework import status, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User, Notification
from .serializers import (
    UserSerializer,
    LoginSerializer,
    NotificationSerializer,
)


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        return super().get_serializer_class()

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=[AllowAny],
    )
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            serializer.is_valid(raise_exception=True)
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(access_token),
                },
                status=status.HTTP_200_OK,
            )


class NotificationViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get(self):
        return Notification.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )

    @action(detail=False, methods=["GET"])
    def not_viewed_count(self, request):
        return Response(
            {
                "not_viewed_count": Notification.objects.filter(
                    user=request.user, viewed=False
                ).count()
            },
            status=status.HTTP_200_OK,
        )
