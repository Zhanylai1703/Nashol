from rest_framework import serializers

from apps.bitches.models import (
    Category,
    Bitch,
    Image,
)


class Imageserializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'photo',
            'is_preview',
        )


class BitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitch
        fields = (
            'id',
            'name',
            'description',
            'price',
            'author',
            'category',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent',
        )