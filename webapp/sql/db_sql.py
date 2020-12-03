from django.db import DatabaseError, transaction
from colddeviceapp.models import ColdDeviceType, ColdDevice, Compartment
from userapp.models import TypeList, CustomUser
from prodapp.models import Category, SubCategory, Product, IndustrialProduct
from stockapp.models import Stock, Diary, Notification
from webapp.utilities.api.requester import Requester
from webapp.utilities.api.product_data import Product_data
import webapp.utilities.data as dt
import logging
import datetime


class Sql():

    def device_type_builder():
        """"""
        logger = logging.getLogger(__name__)
        type_list = ["Congélateur bac", "Congélateur tiroir"]

        for elem in type_list:
            new_type = ColdDeviceType(colddevicetype_name=elem)
            try:
                with transaction.atomic():
                    new_type.save()
            except DatabaseError as insert_error:
                logger.error(insert_error)
                pass

    def user_type_builder():
        """"""
        logger = logging.getLogger(__name__)
        type_list = ["particulier", "professionel"]

        for elem in type_list:
            new_type = TypeList(type_name=elem)
            try:
                with transaction.atomic():
                    new_type.save()
            except DatabaseError as insert_error:
                logger.error(insert_error)
                pass

    def device_creation(data):
        logger = logging.getLogger(__name__)
        device_type = ColdDeviceType.objects.get(
            colddevicetype_name=data["device_type"]
        )
        user = CustomUser.objects.get(username=data["user"])
        device = ColdDevice(
            colddevice_name=data["device_name"],
            colddevice_place=data["device_place"],
            colddevice_user=user,
            colddevice_type=device_type
        )
        try:
            with transaction.atomic():
                device.save()
        # report error if not ok
        except DatabaseError as prod_error:
            logger.error(prod_error)
            pass

        for elem in data["compart_list"]:
            compartment = Compartment(
                compartment_name=elem,
                compartment_colddevice=device,
            )
            try:
                with transaction.atomic():
                    compartment.save()
            # report error if not ok
            except DatabaseError as prod_error:
                logger.error(prod_error)
                pass

    def category_builder():
        logger = logging.getLogger(__name__)
        category_list = ["industriel", "viande", "poisson", "legume", "autre"]
        for category in category_list:
            new_category = Category(category_name=category)
            try:
                with transaction.atomic():
                    new_category.save()
            except DatabaseError as insert_error:
                logger.error(insert_error)
                pass

    def subcategory_builder():
        logger = logging.getLogger(__name__)
        data_dict = dt.data_dict
        for categories in data_dict:
            category = Category.objects.get(category_name=categories)
            for subcategory in data_dict[categories]["subcategory"]:
                new_subcategory = SubCategory(
                    subcategory_category=category,
                    subcategory_name=subcategory["name"],
                    subcategory_peremption=subcategory["duration"],
                )
                try:
                    with transaction.atomic():
                        new_subcategory.save()
                except DatabaseError as insert_error:
                    logger.error(insert_error)
                    pass

    def product_creation(data):
        logger = logging.getLogger(__name__)
        subcategory = SubCategory.objects.get(
            subcategory_name=data["subcategory"]
        )
        user = CustomUser.objects.get(username=data["user"])
        product = Product(
            product_subcategory=subcategory,
            product_name=data["product_name"],
            user_product=user
        )
        try:
            with transaction.atomic():
                product.save()
        except DatabaseError as insert_error:
            logger.error(insert_error)
            pass

    def stockage(data):
        logger = logging.getLogger(__name__)
        notification_date = datetime.datetime.strptime(
            data["date"], '%d/%m/%Y'
        )
        diary = Diary(
            diary_add=datetime.datetime.now().date(),
            diary_number=0,
        )
        notification = Notification(
            notification_date=notification_date,
            notification_is_send=0,
        )
        stockage = Stock(
            stock_product=data["product"],
            stock_compartment=data["compartment"],
            stock_number=int(data["product_quantity"]),
            stock_diary=diary,
            stock_notification=notification,
        )
        try:
            with transaction.atomic():
                diary.save()
                notification.save()
                stockage.save()
        except DatabaseError as insert_error:
            logger.error(insert_error)
            pass

    def product_updater():
        """Makes new product insertion in database"""
        # setting the logger
        logger = logging.getLogger(__name__)
        # emptying the database
        categories = Category.objects.all().exclude(
            category_name="industriel"
        ).exclude(category_name="autre")
        # for each category in category list
        for elem in categories:
            id_list = Requester(str(elem)).product_id_list
            # for each product id in id list
            for product_id in id_list:
                # gather product data with Requester class
                product_data = Product_data(
                    Requester.product_data_requester(product_id)
                )
                # create a product in database
                product = IndustrialProduct(
                    ind_product_name=product_data.name,
                    ind_product_url=product_data.url,
                    ind_product_id=product_data.product_id,
                )
                # save if ok
                try:
                    with transaction.atomic():
                        product.save()
                # report error if not ok
                except DatabaseError as prod_error:
                    logger.error(prod_error)
                    pass

    def remove_device(device_id):
        logger = logging.getLogger(__name__)
        device = ColdDevice.objects.get(id=device_id)
        try:
            with transaction.atomic():
                device.delete()
        # report error if not ok
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass

    def remove_compartment(compartment_id):
        logger = logging.getLogger(__name__)
        compartment = Compartment.objects.get(id=compartment_id)
        try:
            with transaction.atomic():
                compartment.delete()
        # report error if not ok
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass

    def remove_stock(stock_id):
        logger = logging.getLogger(__name__)
        stock = Stock.objects.get(id=stock_id)
        stock.stock_number -= 1
        diary = stock.stock_diary
        notification = stock.stock_notification
        if stock.stock_number == 0:
            diary.diary_remove = datetime.datetime.now().date()
            diary.diary_number += 1
            notification.notification_is_send = 1
            try:
                with transaction.atomic():
                    stock.save()
                    diary.save()
                    notification.save()
            # report error if not ok
            except DatabaseError as remove_error:
                logger.error(remove_error)
                pass
        else:
            diary.diary_modification = datetime.datetime.now().date()
            diary.diary_number += 1
            try:
                with transaction.atomic():
                    diary.save()
                    stock.save()
            # report error if not ok
            except DatabaseError as remove_error:
                logger.error(remove_error)
                pass

    def notification_is_send(notification):
        logger = logging.getLogger(__name__)
        print(notification.notification_is_send)
        notification.notification_is_send = 1
        try:
            with transaction.atomic():
                notification.save()
        except DatabaseError as save_error:
            logger.error(save_error)
            pass

    def destroy_stock(diary):
        logger = logging.getLogger(__name__)
        stock = Stock.objects.get(stock_diary=diary)
        notification = stock.stock_notification
        try:
            with transaction.atomic():
                stock.delete()
                notification.delete()
                diary.delete()
        # report error if not ok
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass
