from django.test import TestCase
from django.urls import reverse
from prodapp.models import Category, SubCategory, Product
from userapp.models import CustomUser


class AjaxStoragePageTestCase(TestCase):

    def test_ajax_storage_returns_200(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
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
            reverse("ajax_storage"),
            {"product": product.id},
        )

        self.assertEqual(response.status_code, 200)
