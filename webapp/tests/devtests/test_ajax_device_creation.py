from django.test import TestCase
from django.urls import reverse


class AjaxDeviceCreationPageTestCase(TestCase):
    def test_ajax_device_creation_returns_200(self):

        response = self.client.get(reverse("ajax_device_creation"))
        self.assertEqual(response.status_code, 200)
