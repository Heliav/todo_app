from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User, Notification


class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

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

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #
    #     return attrs

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         date_of_birth=validated_data['date_of_birth'],
    #         mobile_phone=validated_data['mobile_phone']
    #     )
    #
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     return user


# class RegisterSerializer(serializers.ModelSerializer):
# class Meta:
#     model = User

#     fields = ("username", "password", "email")
#     extra_kwargs = {"password": {"write_only": True}}
#
# def create(self, validated_data):
#     user = User.objects.create_user(
#         validated_data["username"],
#         validated_data["email"],
#         validated_data["password"],
#     )
#     Token.objects.create(user=user)
#     return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
