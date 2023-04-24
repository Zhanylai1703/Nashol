from django.db import models
from django_editorjs import EditorJsField

from apps.common.models import AbstractBaseModel
from apps.users.models import User


class Category(AbstractBaseModel):
    name = models.CharField(
        max_length=120, 
        verbose_name='название'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='children', blank=True, null=True,
        verbose_name='Родительская категория'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Bitch(AbstractBaseModel):
    name = models.CharField(
        max_length=120, 
        verbose_name='название',
    )
    description = EditorJsField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='цена'
    )
    author = models.ForeignKey(
        User, related_name='bitches',
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='bitches',
        verbose_name='категория'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return self.name
    

class Image(AbstractBaseModel):
    photo = models.FileField(
        upload_to='images/%Y/%m/%d/', 
        verbose_name='Фото'
    )
    bitch = models.ForeignKey(
        Bitch, related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    is_preview = models.BooleanField(
        default=False, verbose_name='Превью'
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'
    
    def __str__(self):
        return self.bitch
