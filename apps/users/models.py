from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from apps.common.constants import UserType
from apps.common.models import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    number = models.CharField(
        max_length=60 ,
        verbose_name='номер телефона'
    )
    type = models.CharField(
        max_length=10, choices=UserType.choices,
        verbose_name='Тип пользователя',
        default=UserType.CONSUMER
    )
    geo = models.CharField(
        max_length=100, null=True, blank=True, 
        verbose_name='геолокация'
    )
    rathing = models.PositiveIntegerField(
        default=0, blank=True, null=True,
        verbose_name='Рейтинг'
    )
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return f'{self.username}, Tel: {self.number}'
    
    def clean(self):
        super().clean()
        if self.type == UserType.PRODUSER:
            if self.geo is None:
                raise validators.ValidationError(
                    'You are finder, the field geo is required'
                )
            if self.rathing is None:
                raise validators.ValidationError(
                    'You are finder, the field rathing is required'
                )
            
