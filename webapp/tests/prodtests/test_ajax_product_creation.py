from django.test import TestCase
from django.urls import reverse
from prodapp.models import Category, SubCategory


class AjaxProductCreationPageTestCase(TestCase):

    def test_ajax_product_creation_returns_200(self):

        category = Category.objects.create(
            category_name="fakecat",
        )

        subcategory = SubCategory.objects.create(
            subcategory_category=category,
            subcategory_name="fakesubcat",
            subcategory_peremption=30,
        )

        response = self.client.get(
            reverse("ajax_product_creation"),
            {
                "subcategory": subcategory.id,
                "checker": "raw",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_ajax_product_creation_contains_subcategory(self):

        category = Category.objects.create(
            category_name="fakecat",
        )

        subcategory = SubCategory.objects.create(
            subcategory_category=category,
            subcategory_name="fakesubcat",
            subcategory_peremption=30,
        )

        response = self.client.get(
            reverse("ajax_product_creation"),
            {
                "subcategory": subcategory.id,
                "checker": "raw",
            },
        )
        self.assertContains(response, "fakesubcat")
