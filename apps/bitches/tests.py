from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from apps.bitches.models import (
    Bitch, 
    Category, 
    Image
    )

from apps.users.models import User


class BitchTest(APITestCase):

    def setUp(self):
        print('urls.py imported successfully')
        self.user = User.objects.create(
            username='test',
            email='test@gmail.com',
            number='+996703443555',
            password='123123'
        )
        self.category = Category.objects.create(name='root')
        self.client.force_authenticate(user=self.user)

    def test_getting_bitches_list(self):
        bitch_1 = Bitch.objects.create(
            name='bitch_1',
            description='bitch_1',
            price='100',
            author=self.user,
            category=self.category,
        )
        bitch_2 = Bitch.objects.create(
            name='bitch_2',
            description='bitch_2',
            price='100',
            author=self.user,
            category=self.category,
        )
        responce = self.client.get(reverse('bitches-list'))
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json()[0]['id'], str(bitch_1.id))
        self.assertEqual(responce.json()[1]['id'], str(bitch_2.id))


class CategotyTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            email='test@gmail.com',
            number='+996703443555',
            password='123123'
        )
        self.client = APIClient()
        self.url = reverse('category-list')
        self.category = Category.objects.create(name='test_category')
        self.client.force_authenticate(user=self.user)

    def test_create_category(self):
        category1 = {
            'name': 'new_category', 
            'parent': str(self.category.id)}
        category2 = {
            'name': 'new_category', 
            'parent': str(self.category.id)}
        response = self.client.post(self.url, data=category1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_delete_category(self):
        response = self.client.delete(f'{self.url}{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


