from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from apps.users.factories import UserFactory
from apps.users.factories import UserFactory
from apps.users.models import User


class UserTestCase(APITestCase):
    def test_user_creation(self):
        user = UserFactory()
        self.assertIsInstance(user, get_user_model())
        self.assertTrue(user.username.startswith('user'))
        self.assertTrue(user.check_password('password123'))

