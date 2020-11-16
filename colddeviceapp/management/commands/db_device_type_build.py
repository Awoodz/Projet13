from django.core.management.base import BaseCommand
import logging

from django.db import DatabaseError, transaction
from colddeviceapp.models import ColdDeviceType


class Command(BaseCommand):

    def handle(self, *args, **options):

        logger = logging.getLogger(__name__)

        type_list = ["Congélateur bac", "Congélateur tiroir"]

        for elem in type_list:
            new_type = ColdDeviceType(colddevicetype_name=elem)
            try:
                with transaction.atomic():
                    new_type.save()
            except DatabaseError as insert_error:
                logger.error(insert_error)
                pass
