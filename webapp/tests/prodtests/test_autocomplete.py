from django.test import TestCase
from django.urls import reverse

from prodapp.models import IndustrialProduct


class ProductAutocompletePageTestCase(TestCase):
    def test_product_autocomplete_returns_200(self):

        response = self.client.get(reverse("autocomplete"))
        self.assertEqual(response.status_code, 200)

    def test_product_autocomplete_contains_product(self):

        product = IndustrialProduct.objects.create(
            ind_product_name="fakeprod",
            ind_product_url="fakeurl",
            ind_product_id="fakeid",
        )

        response = self.client.get(reverse("autocomplete"))
        self.assertEqual(
            response.json(),
            {
                "results": [
                    {
                        "id": str(product.id),
                        "text": "fakeprod",
                        "selected_text": "fakeprod",
                    }
                ],
                "pagination": {"more": False},
            },
        )
