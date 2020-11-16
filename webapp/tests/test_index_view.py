from django.test import TestCase
from django.urls import reverse


class IndexPageTestCase(TestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
