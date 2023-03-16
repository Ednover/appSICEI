from rest_framework import status
from django.urls import reverse
from django.test import SimpleTestCase
from api.views import students

class TestQueryStudents(SimpleTestCase):
    def test_get_students(self):
        url = reverse('alumnos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(students))
        