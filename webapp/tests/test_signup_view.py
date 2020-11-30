from django.test import TestCase
from django.urls import reverse


class SignupPageTestCase(TestCase):
    def test_signup_returns_200(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
