from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from userapp.models import CustomUser
from webapp.models import AppNews


class AxajCreateNewsPageTestCase(TestCase):
    def test_ajax_create_news_returns_json(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
            is_staff="t",
        )

        AppNews.objects.create(
            news_title="faketitle",
            news_date=datetime.now().date(),
            news_author=user,
            news_content="fakecontent",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("ajax_create_news"))

        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_create_news_creates_news(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
            is_staff="t",
        )

        self.client.force_login(user)

        count = AppNews.objects.all().count()
        self.assertEqual(count, 0)

        self.client.get(
            reverse("ajax_create_news"),
            {
                "title": "faketitle",
                "content": "fakecontent",
            },
        )

        count = AppNews.objects.all().count()
        self.assertEqual(count, 1)
