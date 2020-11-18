from django.db import models
from userapp.models import CustomUser


class ColdDeviceType(models.Model):
    colddevicetype_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.colddevicetype_name


class ColdDevice(models.Model):
    colddevice_name = models.CharField(max_length=100)
    colddevice_place = models.CharField(max_length=100)
    colddevice_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    colddevice_type = models.ForeignKey(
        ColdDeviceType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.colddevice_name


class Compartment(models.Model):
    compartment_name = models.CharField(max_length=100)
    compartment_colddevice = models.ForeignKey(
        ColdDevice,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.compartment_name
