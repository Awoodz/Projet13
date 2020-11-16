from userapp.models import CustomUser

from django.db import models


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
    user_product = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.product_name
