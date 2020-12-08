from django.test import TestCase
from prodapp.models import Category
from webapp.sql.db_sql import Sql


class CategoryBuilderTestCase(TestCase):

    def test_category_builder_creates_category(self):
        count = Category.objects.all().count()
        self.assertEqual(count, 0)
        Sql.category_builder()
        count = Category.objects.all().count()
        self.assertGreater(count, 0)
