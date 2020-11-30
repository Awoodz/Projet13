from django.test import TestCase
from django.urls import reverse


class LoginPageTestCase(TestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
