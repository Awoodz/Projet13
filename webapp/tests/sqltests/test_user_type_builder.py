from django.test import TestCase
from userapp.models import TypeList
from webapp.sql.db_sql import Sql


class UserTypeBuilderTestCase(TestCase):

    def test_user_type_builder_creates_user_type(self):
        count = TypeList.objects.all().count()
        self.assertEqual(count, 0)
        Sql.user_type_builder()
        count = TypeList.objects.all().count()
        self.assertEqual(count, 2)
