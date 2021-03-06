from django.core.management.base import BaseCommand

from webapp.sql.db_sql import Sql


class Command(BaseCommand):
    """Fulfill database with necessary data"""

    def handle(self, *args, **options):
        Sql.device_type_builder()
        Sql.user_type_builder()
        Sql.category_builder()
        Sql.subcategory_builder()
        Sql.product_updater()
