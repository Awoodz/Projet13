from django.test import TestCase
from django.urls import reverse

from prodapp.models import Category, Product, SubCategory
from userapp.models import CustomUser


class AjaxCreateProductPageTestCase(TestCase):

    def test_ajax_create_product_returns_JSON(self):

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

        response = self.client.get(
            reverse("ajax_create_product"),
            {
                "checker": "raw",
                "subcategory": subcategory,
                "product_name": "fakeprod",
            },
        )
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_ajax_create_product_creates_product(self):

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

        prodcount = Product.objects.all().count()
        self.assertEqual(prodcount, 0)

        self.client.get(
            reverse("ajax_create_product"),
            {
                "checker": "raw",
                "subcategory": subcategory,
                "product_name": "fakeprod",
            },
        )

        prodcount = Product.objects.all().count()
        self.assertEqual(prodcount, 1)
