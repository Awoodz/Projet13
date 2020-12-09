from django.db import models

from userapp.models import CustomUser


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    subcategory_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    subcategory_name = models.CharField(max_length=100, unique=True)
    subcategory_peremption = models.IntegerField()

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    product_subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=100)
    user_product = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product_name


class IndustrialProduct(models.Model):
    ind_product_name = models.CharField(max_length=100, unique=True)
    ind_product_url = models.CharField(max_length=200, unique=True)
    ind_product_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ind_product_name
