from datetime import datetime, timedelta

from django.test import TestCase

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, Product, SubCategory
from stockapp.models import Diary, Notification, Stock
from userapp.models import CustomUser
from webapp.sql.db_cleaner import db_clean_stocks


class DbCleanStocksTestCase(TestCase):

    def test_db_clean_stocks_cleans_old_stocks(self):

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

        fake_date1 = datetime.now().date() - timedelta(days=91)

        diary1 = Diary.objects.create(
            diary_add=fake_date1,
            diary_remove=fake_date1,
            diary_number=0,
        )

        notification1 = Notification.objects.create(
            notification_date=fake_date1,
            notification_is_send=1,
        )

        stock1 = Stock.objects.create(
            stock_product=product,
            stock_compartment=compartment,
            stock_number=1,
            stock_diary=diary1,
            stock_notification=notification1,
        )

        fake_date2 = datetime.now().date() - timedelta(days=89)

        diary2 = Diary.objects.create(
            diary_add=fake_date2,
            diary_remove=fake_date2,
            diary_number=0,
        )

        notification2 = Notification.objects.create(
            notification_date=fake_date2,
            notification_is_send=1,
        )

        stock2 = Stock.objects.create(
            stock_product=product,
            stock_compartment=compartment,
            stock_number=1,
            stock_diary=diary2,
            stock_notification=notification2,
        )

        count = Stock.objects.all().count()
        self.assertEqual(count, 2)

        db_clean_stocks()

        count = Stock.objects.all().count()
        self.assertEqual(count, 1)
