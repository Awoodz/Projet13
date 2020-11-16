from django.db import models
from prodapp.models import Product
from colddeviceapp.models import Compartment


class Stock(models.Model):
    stock_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    stock_compartment = models.ForeignKey(
        Compartment,
        on_delete=models.CASCADE
    )
    stock_number = models.IntegerField()


class Diary(models.Model):
    diary_stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE
    )
    diary_add = models.DateField(auto_now=False, auto_now_add=False)
    diary_modification = models.DateField(auto_now=False, auto_now_add=False)
    diary_remove = models.DateField(auto_now=False, auto_now_add=False)
    diary_number = models.IntegerField()


class Notification(models.Model):
    notification_stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE
    )
    notification_date = models.DateField(auto_now=False, auto_now_add=False)
    notification_is_send = models.IntegerField()
