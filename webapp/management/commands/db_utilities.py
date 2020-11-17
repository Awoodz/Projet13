from django.db import DatabaseError, transaction
from colddeviceapp.models import ColdDeviceType
from userapp.models import TypeList


def device_type_builder(logger):
    """"""
    type_list = ["Congélateur bac", "Congélateur tiroir"]

    for elem in type_list:
        new_type = ColdDeviceType(colddevicetype_name=elem)
        try:
            with transaction.atomic():
                new_type.save()
        except DatabaseError as insert_error:
            logger.error(insert_error)
            pass


def user_type_builder(logger):
    """"""
    type_list = ["particulier", "professionel"]

    for elem in type_list:
        new_type = TypeList(type_name=elem)
        try:
            with transaction.atomic():
                new_type.save()
        except DatabaseError as insert_error:
            logger.error(insert_error)
            pass
