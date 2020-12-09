from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, Product, SubCategory
from stockapp.models import Diary, Notification, Stock
from userapp.models import CustomUser


class AjaxStockedPageTestCase(TestCase):

    def test_ajax_stocked_returns_JSON(self):

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

        category = Category.objects.create(
            category_name="fakecat",
        )

        subcategory = SubCategory.objects.create(
            subcategory_category=category,
            subcategory_name="fakesubcat",
            subcategory_peremption=30,
        )

        product = Product.objects.create(
            product_name="fakeprod",
            product_subcategory=subcategory,
            user_product=user,
        )

        response = self.client.get(
            reverse("ajax_stocked"),
            {
                "compartment": compartment.id,
                "product": product.id,
                "product_quantity": "1",
                "date": "01/12/2020",
            },
        )
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_ajax_stocked_creates_stock(self):

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

        category = Category.objects.create(
            category_name="fakecat",
        )

        subcategory = SubCategory.objects.create(
            subcategory_category=category,
            subcategory_name="fakesubcat",
            subcategory_peremption=30,
        )

        product = Product.objects.create(
            product_name="fakeprod",
            product_subcategory=subcategory,
            user_product=user,
        )

        count = Stock.objects.all().count()
        self.assertEqual(count, 0)

        response = self.client.get(
            reverse("ajax_stocked"),
            {
                "compartment": compartment.id,
                "product": product.id,
                "product_quantity": "1",
                "date": "01/12/2020",
            },
        )

        count = Stock.objects.all().count()
        self.assertEqual(count, 1)
