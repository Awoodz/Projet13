from django.test import TestCase
from django.urls import reverse
from userapp.models import CustomUser
from colddeviceapp.models import ColdDevice, ColdDeviceType


class AjaxCreateDevicePageTestCase(TestCase):
    def test_ajax_create_device_returns_JSON(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )

        self.client.force_login(user)

        device_type = ColdDeviceType.objects.create(
            colddevicetype_name="faketype",
        )

        response = self.client.get(
            reverse("ajax_create_device"),
            {
                "device_name": "fakedevice",
                "device_place": "fakeplace",
                "device_type": "faketype",
                "compart_number": 2,
                "compart_list": '["fakecompartment", "fakecompartment2"]'
            },
        )

        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_ajax_create_device_creates_device(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )

        self.client.force_login(user)

        device_type = ColdDeviceType.objects.create(
            colddevicetype_name="faketype",
        )

        response = self.client.get(
            reverse("ajax_create_device"),
            {
                "device_name": "fakedevice",
                "device_place": "fakeplace",
                "device_type": "faketype",
                "compart_number": 2,
                "compart_list": '["fakecompartment", "fakecompartment2"]'
            },
        )

        device = ColdDevice.objects.get(colddevice_name="fakedevice")
        self.assertEqual(device.colddevice_place, "fakeplace")
