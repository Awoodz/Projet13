from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from userapp.models import CustomUser
from webapp.models import AppNews


class AxajDestroyNewsPageTestCase(TestCase):
    def test_ajax_destroy_news_returns_json(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
            is_staff="t",
        )

        news = AppNews.objects.create(
            news_title="faketitle",
            news_date=datetime.now().date(),
            news_author=user,
            news_content="fakecontent",
        )

        self.client.force_login(user)

        response = self.client.get(
            reverse("ajax_destroy_news"),
            {
                "news": news.id,
            },
        )

        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'success'}
        )

    def test_create_destroy_destroys_news(self):

        user = CustomUser.objects.create(
            username="fakeuser",
            email="fakemail@mail.com",
            password="fakepassword",
            is_staff="t",
        )

        news = AppNews.objects.create(
            news_title="faketitle",
            news_date=datetime.now().date(),
            news_author=user,
            news_content="fakecontent",
        )

        self.client.force_login(user)

        count = AppNews.objects.all().count()
        self.assertEqual(count, 1)

        self.client.get(
            reverse("ajax_destroy_news"),
            {
                "news": news.id,
            },
        )

        count = AppNews.objects.all().count()
        self.assertEqual(count, 0)
