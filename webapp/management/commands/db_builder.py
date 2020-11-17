from django.core.management.base import BaseCommand
from webapp.sql.db_sql import Sql


class Command(BaseCommand):

    def handle(self, *args, **options):
        Sql.device_type_builder()
        Sql.user_type_builder()
