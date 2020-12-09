from django.test import TestCase

from colddeviceapp.models import ColdDeviceType
from webapp.sql.db_sql import Sql


class DeviceTypeBuilderTestCase(TestCase):

    def test_device_type_builder_creates_device_type(self):
        count = ColdDeviceType.objects.all().count()
        self.assertEqual(count, 0)
        Sql.device_type_builder()
        count = ColdDeviceType.objects.all().count()
        self.assertEqual(count, 2)
