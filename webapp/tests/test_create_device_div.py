from django.test import TestCase
from django.urls import reverse
from colddeviceapp.models import ColdDevice, ColdDeviceType
from userapp.models import CustomUser


class DeviceDivPageTestCase(TestCase):
    def test_device_div_returns_200(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )

        self.client.force_login(user)

        device_type = ColdDeviceType.objects.create(
            colddevicetype_name="faketype",
        )

        device = ColdDevice.objects.create(
            colddevice_name="fakedevice",
            colddevice_place="fakeplace",
            colddevice_user=user,
            colddevice_type=device_type,
        )

        response = self.client.get(reverse("device"), {"checker": "none"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fakedevice")
