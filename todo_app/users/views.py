from django.contrib.auth import authenticate, logout
from rest_framework import status, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_app.users.models import User, Notification
from .serializers import UserSerializer, LoginSerializer, NotificationSerializer


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        mobile_phone = request.data.get("mobile_phone")
        username = request.data.get("username")

        if not mobile_phone or not username:
            return Response(
                {"error": "mobile phone and username are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        existing_user = User.objects.filter(
            mobile_phone=mobile_phone, username=username
        ).first()
        if existing_user:
            serializer = self.get_serializer(existing_user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        user = User.objects.create(mobile_phone=mobile_phone, username=username)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data["username"]
            password = serializer.data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class NotificationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )

    @action(detail=False, methods=["get"])
    def not_viewed_count(self, request):
        return Response(
            {
                "not_viewed_count": Notification.objects.filter(
                    user=request.user, viewed=False
                ).count()
            },
            status=status.HTTP_200_OK,
        )
