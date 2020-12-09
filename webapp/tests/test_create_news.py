from django.test import TestCase
from django.urls import reverse

from userapp.models import CustomUser


class CreateNewsPageTestCase(TestCase):
    def test_create_news_returns_JSON(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
            is_staff="t",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("create_news"))

        self.assertEqual(response.status_code, 200)
