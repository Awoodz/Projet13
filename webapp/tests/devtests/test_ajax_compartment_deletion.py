from django.test import TestCase
from django.urls import reverse

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from userapp.models import CustomUser


class AjaxCompartmentDeletionPageTestCase(TestCase):
    def test_ajax_compartment_deletion_returns_JSON(self):

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

        response = self.client.get(
            reverse("ajax_compartment_deletion"),
            {"compartment": compartment.id},
        )
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_ajax_compartment_deletion_deletes_compartment(self):

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

        self.client.get(
            reverse("ajax_compartment_deletion"),
            {"compartment": compartment.id},
        )

        count = Compartment.objects.all().count()
        self.assertEqual(count, 0)
