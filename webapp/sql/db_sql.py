from django.db import DatabaseError, transaction
from colddeviceapp.models import ColdDeviceType, ColdDevice, Compartment
from userapp.models import TypeList, CustomUser
import logging


class Sql():

    def device_type_builder():
        """"""
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

    def user_type_builder():
        """"""
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

    def device_creation(data):
        logger = logging.getLogger(__name__)
        device_type = ColdDeviceType.objects.get(
            colddevicetype_name=data["device_type"]
        )
        user = CustomUser.objects.get(username=data["user"])
        device = ColdDevice(
            colddevice_name=data["device_name"],
            colddevice_place=data["device_place"],
            colddevice_user=user,
            colddevice_type=device_type
        )
        try:
            with transaction.atomic():
                device.save()
        # report error if not ok
        except DatabaseError as prod_error:
            logger.error(prod_error)
            pass

        for elem in data["compart_list"]:
            compartment = Compartment(
                compartment_name=elem,
                compartment_colddevice=device,
            )
            try:
                with transaction.atomic():
                    compartment.save()
            # report error if not ok
            except DatabaseError as prod_error:
                logger.error(prod_error)
                pass
