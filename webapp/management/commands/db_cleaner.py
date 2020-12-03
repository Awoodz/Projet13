from django.core.management.base import BaseCommand
from webapp.sql.db_cleaner import db_clean_stocks


class Command(BaseCommand):

    def handle(self, *args, **options):
        db_clean_stocks()
