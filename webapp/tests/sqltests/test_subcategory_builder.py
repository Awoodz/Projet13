from django.test import TestCase
from prodapp.models import SubCategory
from webapp.sql.db_sql import Sql


class SubCategoryBuilderTestCase(TestCase):

    def test_subcategory_builder_creates_category(self):
        Sql.category_builder()
        count = SubCategory.objects.all().count()
        self.assertEqual(count, 0)
        Sql.subcategory_builder()
        count = SubCategory.objects.all().count()
        self.assertGreater(count, 0)
