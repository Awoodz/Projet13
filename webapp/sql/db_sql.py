import datetime
import logging

from django.db import DatabaseError, transaction

import webapp.utilities.data as dt
from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, IndustrialProduct, Product, SubCategory
from stockapp.models import Diary, Notification, Stock
from userapp.models import CustomUser, TypeList
from webapp.models import AppNews
from webapp.utilities.api.product_data import Product_data
from webapp.utilities.api.requester import Requester


class Sql():

    def device_type_builder():
        """Add device types to database"""
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
        """Add user types to database"""
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
        """Add user's device to database"""
        logger = logging.getLogger(__name__)

        # Get the device type
        device_type = ColdDeviceType.objects.get(
            colddevicetype_name=data["device_type"]
        )
        # Get the device user
        user = CustomUser.objects.get(username=data["user"])
        # Creates the device
        device = ColdDevice(
            colddevice_name=data["device_name"],
            colddevice_place=data["device_place"],
            colddevice_user=user,
            colddevice_type=device_type
        )
        try:
            with transaction.atomic():
                device.save()
        except DatabaseError as prod_error:
            logger.error(prod_error)
            pass

        # For compartments in device
        for elem in data["compart_list"]:
            # Creates compartments
            compartment = Compartment(
                compartment_name=elem,
                compartment_colddevice=device,
            )
            try:
                with transaction.atomic():
                    compartment.save()
            except DatabaseError as prod_error:
                logger.error(prod_error)
                pass

    def category_builder():
        """Add food category to database"""
        logger = logging.getLogger(__name__)
        # Get categories names from dictionnary
        for category in dt.DATA_DICT:
            # Creates category for each element
            new_category = Category(category_name=category)
            try:
                with transaction.atomic():
                    new_category.save()
            except DatabaseError as insert_error:
                logger.error(insert_error)
                pass

    def subcategory_builder():
        logger = logging.getLogger(__name__)
        # Get categories names from dictionnary
        for categories in dt.DATA_DICT:
            # Get category for each element
            category = Category.objects.get(category_name=categories)
            # Get subcategories datas from dictionnary
            for subcategory in dt.DATA_DICT[categories]["subcategory"]:
                # Creates subcategory for each element
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
        # Get the product subcategory
        subcategory = SubCategory.objects.get(
            subcategory_name=data["subcategory"]
        )
        # Get the product user
        user = CustomUser.objects.get(username=data["user"])
        # Creates the product
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
        # Converts date to date type var
        notification_date = datetime.datetime.strptime(
            data["date"], '%d/%m/%Y'
        )
        # Creates a product diary
        diary = Diary(
            diary_add=datetime.datetime.now().date(),
            diary_number=0,
        )
        # Creates a notification rememberer
        notification = Notification(
            notification_date=notification_date,
            notification_is_send=0,
        )
        # Creates a stock
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
        """Insert openfoodfact products in database"""
        logger = logging.getLogger(__name__)
        category = "surgeles"
        id_list = Requester(str(category)).product_id_list
        # For each product in list
        for product_id in id_list:
            # Get product datas
            product_data = Product_data(
                Requester.product_data_requester(product_id)
            )
            # Creates product in database
            product = IndustrialProduct(
                ind_product_name=product_data.name,
                ind_product_url=product_data.url,
                ind_product_id=product_data.product_id,
            )
            try:
                with transaction.atomic():
                    product.save()
            except DatabaseError as prod_error:
                logger.error(prod_error)
                pass

    def remove_device(device_id):
        """Removes user's device from database"""
        logger = logging.getLogger(__name__)
        # Get the device then removes it
        device = ColdDevice.objects.get(id=device_id)
        compartments = Compartment.objects.filter(
            compartment_colddevice=device
        )
        for compartment in compartments:
            stocks = Stock.objects.filter(stock_compartment=compartment)
            for stock in stocks:
                notification = stock.stock_notification
                diary = stock.stock_diary
                try:
                    with transaction.atomic():
                        notification.delete()
                        diary.delete()
                except DatabaseError as remove_error:
                    logger.error(remove_error)
                    pass
        try:
            with transaction.atomic():
                device.delete()
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass

    def remove_compartment(compartment_id):
        """Removes device's compartment from database"""
        logger = logging.getLogger(__name__)
        # Get the compartment then removes it
        compartment = Compartment.objects.get(id=compartment_id)
        try:
            with transaction.atomic():
                compartment.delete()
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass

    def remove_stock(stock_id):
        """Substract one product from a stock"""
        logger = logging.getLogger(__name__)
        # Get the stock
        stock = Stock.objects.get(id=stock_id)
        # Substract one product
        stock.stock_number -= 1
        # Get the stock diary
        diary = stock.stock_diary
        # Get the stock notification rememberer
        notification = stock.stock_notification
        # If there is 0 product in stock
        if stock.stock_number == 0:
            # Add a remove date in diary
            diary.diary_remove = datetime.datetime.now().date()
            # Add one to diary number
            diary.diary_number += 1
            # Consider that the notification is send
            notification.notification_is_send = 1
            try:
                with transaction.atomic():
                    stock.save()
                    diary.save()
                    notification.save()
            except DatabaseError as remove_error:
                logger.error(remove_error)
                pass
        # Else if some product remains in stock
        else:
            # Add a modification date in diary
            diary.diary_modification = datetime.datetime.now().date()
            # Add one to diary number
            diary.diary_number += 1
            try:
                with transaction.atomic():
                    diary.save()
                    stock.save()
            except DatabaseError as remove_error:
                logger.error(remove_error)
                pass

    def notification_is_send(notification):
        """Set notification_is_send to 1"""
        logger = logging.getLogger(__name__)
        notification.notification_is_send = 1
        try:
            with transaction.atomic():
                notification.save()
        except DatabaseError as save_error:
            logger.error(save_error)
            pass

    def destroy_stock(diary):
        """Removes stock from database"""
        logger = logging.getLogger(__name__)
        # Get the stock
        stock = Stock.objects.get(stock_diary=diary)
        # Get the notification rememberer
        notification = stock.stock_notification
        # Then delete all
        try:
            with transaction.atomic():
                stock.delete()
                notification.delete()
                diary.delete()
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass

    def add_news(news_data):
        """Add news datas in database"""
        logger = logging.getLogger(__name__)
        # Creates a news
        news = AppNews(
            news_title=news_data["title"],
            news_content=news_data["content"],
            news_date=datetime.datetime.now(),
            news_author=news_data["user"],
        )
        try:
            with transaction.atomic():
                news.save()
        except DatabaseError as save_error:
            logger.error(save_error)
            pass

    def destroy_news(news_id):
        """Removes a new from database"""
        logger = logging.getLogger(__name__)
        news = AppNews.objects.get(id=news_id)
        try:
            with transaction.atomic():
                news.delete()
        except DatabaseError as remove_error:
            logger.error(remove_error)
            pass
