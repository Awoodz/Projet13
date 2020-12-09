from django.test import TestCase
from django.urls import reverse

from prodapp.models import Category, Product, SubCategory
from userapp.models import CustomUser


class AjaxProductPageTestCase(TestCase):

    def test_ajax_product_returns_200(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("ajax_product"))
        self.assertEqual(response.status_code, 200)

    def test_ajax_product_contains_product(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )

        self.client.force_login(user)

        category = Category.objects.create(
            category_name="fakecat",
        )

        subcategory = SubCategory.objects.create(
            subcategory_category=category,
            subcategory_name="fakesubcat",
            subcategory_peremption=30,
        )

        Product.objects.create(
            product_name="fakeprod",
            product_subcategory=subcategory,
            user_product=user,
        )

        products = Product.objects.filter(user_product=user)

        response = self.client.get(
            reverse("ajax_product"),
            {
                "products": products,
            },
        )
        self.assertContains(response, "fakeprod")
