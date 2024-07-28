from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, Notification


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "mobile_phone",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=10)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        if username and password:

            user = authenticate(username=username, password=password)
            if user:
                data["user"] = user

            data["user"] = user
        return data


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
