from django.db.models import TextChoices

class UserType(TextChoices):
    PRODUSER = 'PRODUSER'
    CONSUMER = 'CONSUMER'


