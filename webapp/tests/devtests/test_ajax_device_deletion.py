from django.test import TestCase
from django.urls import reverse

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from userapp.models import CustomUser


class AjaxDeviceDeletionPageTestCase(TestCase):
    def test_ajax_device_deletion_returns_JSON(self):

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

        response = self.client.get(
            reverse("ajax_device_deletion"),
            {"device": device.id},
        )
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_ajax_device_deletion_deletes_device(self):

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

        count = ColdDevice.objects.all().count()
        self.assertEqual(count, 1)

        response = self.client.get(
            reverse("ajax_device_deletion"),
            {"device": device.id},
        )

        count = ColdDevice.objects.all().count()
        self.assertEqual(count, 0)

    def test_ajax_device_deletion_deletes_compartment(self):

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

        compartment = Compartment.objects.create(
            compartment_name="fakecompartment",
            compartment_colddevice=device,
        )

        count = Compartment.objects.all().count()
        self.assertEqual(count, 1)

        response = self.client.get(
            reverse("ajax_device_deletion"),
            {"device": device.id},
        )

        count = Compartment.objects.all().count()
        self.assertEqual(count, 0)
