from datetime import datetime

from django.core import mail
from django.test import TestCase

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, Product, SubCategory
from stockapp.models import Diary, Notification, Stock
from userapp.models import CustomUser
from webapp.utilities.emailing.emailing import emailing


class EmailTest(TestCase):

    def test_send_email(self):
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

        diary = Diary.objects.create(
            diary_add=datetime.now().date(),
            diary_number=0,
        )

        notification = Notification.objects.create(
            notification_date=datetime.now().date(),
            notification_is_send=0,
        )

        stock = Stock.objects.create(
            stock_product=product,
            stock_compartment=compartment,
            stock_number=1,
            stock_diary=diary,
            stock_notification=notification,
        )
    
        emailing()

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "MyColdManager - Rappel")
