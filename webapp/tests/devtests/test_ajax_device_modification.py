from django.test import TestCase
from django.urls import reverse


class AjaxDeviceModificationPageTestCase(TestCase):
    def test_ajax_device_modification_returns_JSON(self):

        response = self.client.get(reverse("ajax_device_modification"))
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )
