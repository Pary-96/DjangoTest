from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CRUD


class ProfileViewTestCase(TestCase):
    def test_profile_view(self):
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "jobs/home.html")


# class GetDataViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.data = CRUD.objects.create(name='Test', age=25, designation='Tester')

#     def test_get_data(self):
#         response = self.client.get(reverse('get_data', args=[self.data.pk]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], 'Test')

# class CreateDataViewTestCase(TestCase):
#     def test_create_data(self):
#         data = {'name': 'Test', 'age': 25, 'designation': 'Tester'}
#         response = self.client.post(reverse('create_data'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class UpdateDataViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.data = CRUD.objects.create(name='Test', age=25, designation='Tester')

#     def test_update_data(self):
#         data = {'name': 'Updated', 'age': 30, 'designation': 'Updated Tester'}
#         response = self.client.put(reverse('update_data', args=[self.data.pk]), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class DeleteDataViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.data = CRUD.objects.create(name='Test', age=25, designation='Tester')

#     def test_delete_data(self):
#         response = self.client.delete(reverse('delete_data', args=[self.data.pk]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
