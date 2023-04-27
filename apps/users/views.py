import jwt

from django.conf import settings

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.users.models import User

from apps.users.serializers import (
    Userserializer, 
    RegisterSerializer,
    LoginSerializer,
    LogoutSerializer,
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
            'user_id': str(user.id), 
            'username': user.username
        }
        
        access_token = jwt.encode(
            user_payload, settings.SECRET_KEY, 
            algorithm="HS256"
        )
        refresh_token = jwt.encode(
            user_payload, settings.SECRET_KEY, 
            algorithm="HS256"
        )

        response_data = {
            'user_id': str(user.id),
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
        return Response(
            serializer.validated_data, 
            status=status.HTTP_200_OK
        )
    

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        # Удаление токена доступа пользователя из базы данных или сессии
        request.user.auth_token.delete()
        return Response(
            {'message': 'Вы успешно вышли'}, 
            status=status.HTTP_200_OK
        )