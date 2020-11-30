from django.test import TestCase
from django.urls import reverse
from userapp.models import CustomUser


class ManageStocksPageTestCase(TestCase):
    def test_manage_stocks_returns_200(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
        )
        self.client.force_login(user)
        response = self.client.get(reverse("manage_stocks"))
        self.assertEqual(response.status_code, 200)
