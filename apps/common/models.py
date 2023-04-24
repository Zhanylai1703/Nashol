from django.db import models
from django.utils import timezone

from uuid import uuid4

class AbstractBaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True,
        default=uuid4,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True