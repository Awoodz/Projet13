from django.core.management.base import BaseCommand
import logging

from django.db import DatabaseError, transaction
from userapp.models import TypeList


class Command(BaseCommand):

    def handle(self, *args, **options):

        logger = logging.getLogger(__name__)

        type_list = ["particulier", "professionel"]

        for elem in type_list:
            new_type = TypeList(type_name=elem)
            try:
                with transaction.atomic():
                    new_type.save()
            except DatabaseError as insert_error:
                logger.error(insert_error)
                pass
