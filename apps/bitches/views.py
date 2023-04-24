from django.shortcuts import render

from rest_framework import generics, viewsets

from apps.bitches.serializers import (
    BitchSerializer,
    CategorySerializer,
    Imageserializer
)

from apps.bitches.models import (
    Bitch,
    Category,
    Image,
)


class BitchViewSet(viewsets.ModelViewSet):
    queryset = Bitch.objects.all()
    serializer_class = BitchSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = Imageserializer

