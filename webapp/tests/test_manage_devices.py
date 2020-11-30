from django.test import TestCase
from django.urls import reverse


class ManageDevicesPageTestCase(TestCase):
    def test_manage_devices_returns_200(self):
        response = self.client.get(reverse("manage_devices"))
        self.assertEqual(response.status_code, 200)
