import jwt
from django.shortcuts import render
from django.conf import settings

from rest_framework import generics, viewsets
from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User

from apps.users.serializers import (
    Userserializer, 
    RegisterSerializer,
    LoginSerializer,
    UserTokenSerializer
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user_payload = {
            'user_id': user.id,
            'username': user.username
        }
        access_token = jwt.encode(user_payload, settings.SECRET_KEY, algorithm="HS256")
        refresh_token = jwt.encode(user_payload, settings.SECRET_KEY, algorithm="HS256")

        response_data = {
            'user_id': user.id,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)