from django.test import TestCase
from django.urls import reverse

from colddeviceapp.models import ColdDevice, ColdDeviceType
from userapp.models import CustomUser


class AjaxDevicePageTestCase(TestCase):
    def test_ajax_device_returns_200(self):

        response = self.client.get(reverse("ajax_device"), {"checker": "none"})
        self.assertEqual(response.status_code, 200)

    def test_ajax_device_contains_device(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )

        self.client.force_login(user)

        device_type = ColdDeviceType.objects.create(
            colddevicetype_name="faketype",
        )

        ColdDevice.objects.create(
            colddevice_name="fakedevice",
            colddevice_place="fakeplace",
            colddevice_user=user,
            colddevice_type=device_type,
        )

        response = self.client.get(reverse("ajax_device"), {"checker": "none"})
        self.assertContains(response, "fakedevice")
