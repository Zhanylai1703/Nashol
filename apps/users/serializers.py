from django.conf import settings
from django.db.models import Q

from djoser.serializers import UserCreateSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

from apps.users.models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'number', 
            'type',
            'geo',
            'rathing',
        )


class UserTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    class Meta:
        fields = (
            'access_token',
            'refresh_token',
        )


class RegisterSerializer(UserCreateSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email', 
            'username', 
            'password', 
            )
    

class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username', None)
        password = attrs.get('password')
        user = User.objects.filter(Q(email=email_or_username)|Q(username=email_or_username)).first()
        if user is None:
            raise serializers.ValidationError("User does not exist.")
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")
        refresh = RefreshToken.for_user(user)
        print(refresh)
        data = {
            'user_id': user.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return data
    

class LogoutSerializer(serializers.Serializer):
    message = serializers.CharField(default='Вы успешно вышли')

    class Meta:
        fields = ('message',)