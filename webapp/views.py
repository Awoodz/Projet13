# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from colddeviceapp.models import ColdDevice, ColdDeviceType

# Create your views here.


def index(request):
    """Index page"""
    template = loader.get_template("webapp/index.html")
    return HttpResponse(template.render(request=request))


@login_required
def device(request):
    """Devices list page"""
    template = loader.get_template("webapp/device.html")
    current_user = request.user
    user_devices = ColdDevice.objects.filter(colddevice_user=current_user.id)
    return HttpResponse(template.render(
        {"user_devices": user_devices},
        request=request,
    ))


@login_required
def add_device(request):
    template = loader.get_template("webapp/create_device.html")
    device_types = ColdDeviceType.objects.all()
    return HttpResponse(template.render(
        {"device_types": device_types},
        request=request,
    ))
