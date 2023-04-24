import factory

from django.utils.timezone import now

from decimal import Decimal

from apps.users.factories import UserFactory
from apps.bitches.models import (
    Bitch,
    Category,
    Image
    )


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category {n}')
    parent = None


class BitchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bitch

    name = factory.Sequence(lambda n: f'Bitch {n}')
    description = factory.Sequence(lambda n: f'Description {n}')
    price = Decimal('99.99')
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    created_at = now()
    updated_at = now()