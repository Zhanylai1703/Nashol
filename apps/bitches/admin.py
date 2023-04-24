from django.contrib import admin

from apps.bitches.models import (
    Category,
    Bitch,
    Image,
)


@admin.register(Category)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Bitch)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class WorkAdmin(admin.ModelAdmin):
    pass
