from django.test import TestCase
from django.urls import reverse

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from userapp.models import CustomUser


class AjaxCompartmentPageTestCase(TestCase):

    def test_ajax_compartment_returns_200(self):

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

        # compartment = Compartment.objects.create(
        #     compartment_name="fakecompartment",
        #     compartment_colddevice=device,
        # )

        response = self.client.get(
            reverse("ajax_compartment"),
            {"device": device.id},
        )
        self.assertEqual(response.status_code, 200)

    def test_ajax_compartment_contains_compartment(self):

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
            reverse("ajax_compartment"),
            {"device": device.id},
        )

        self.assertContains(response, "fakecompartment")
