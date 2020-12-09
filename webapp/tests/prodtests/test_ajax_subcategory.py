from django.test import TestCase
from django.urls import reverse

from prodapp.models import Category, SubCategory


class AjaxSubCategoryPageTestCase(TestCase):
    def test_ajax_subcategory_returns_200(self):

        category = Category.objects.create(
            category_name="fakecat",
        )

        other_subcat = SubCategory.objects.create(
            subcategory_name="autre",
            subcategory_category=category,
            subcategory_peremption=0,
        )

        response = self.client.get(
            reverse("ajax_subcategory"),
            {"category": category.id},
        )
        self.assertEqual(response.status_code, 200)

    def test_ajax_subcategory_contains_subcategory(self):

        category = Category.objects.create(
            category_name="fakecat",
        )

        subcategory = SubCategory.objects.create(
            subcategory_category=category,
            subcategory_name="fakesubcat",
            subcategory_peremption=30,
        )

        other_subcat = SubCategory.objects.create(
            subcategory_name="autre",
            subcategory_category=category,
            subcategory_peremption=0,
        )

        response = self.client.get(
            reverse("ajax_subcategory"),
            {"category": category.id},
        )
        self.assertContains(response, "fakesubcat")
