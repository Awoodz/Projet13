from django.test import TestCase
from django.urls import reverse
from prodapp.models import Category


class AjaxCategoryPageTestCase(TestCase):
    def test_ajax_category_returns_200(self):

        response = self.client.get(reverse("ajax_category"))
        self.assertEqual(response.status_code, 200)

    def test_ajax_category_contains_category(self):

        category = Category.objects.create(
            category_name="fakecat",
        )

        response = self.client.get(reverse("ajax_category"))
        self.assertContains(response, "fakecat")
