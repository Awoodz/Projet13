from django.core.management.base import BaseCommand
import logging
import webapp.management.commands.db_utilities as dbu


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        dbu.device_type_builder(logger)
        dbu.user_type_builder(logger)
