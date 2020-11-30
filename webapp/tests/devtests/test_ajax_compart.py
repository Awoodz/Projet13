from django.test import TestCase
from django.urls import reverse


class AjaxCompartPageTestCase(TestCase):
    def test_ajax_compart_returns_200(self):

        response = self.client.get(
            reverse("ajax_compart"),
            {"compartment": "2"},
        )
        self.assertEqual(response.status_code, 200)
