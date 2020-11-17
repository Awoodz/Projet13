import json
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from colddeviceapp.models import ColdDevice, ColdDeviceType
from webapp.sql.db_sql import Sql


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
def create_device(request):
    template = loader.get_template("webapp/create_device.html")
    device_types = ColdDeviceType.objects.all()
    return HttpResponse(template.render(
        {"device_types": device_types},
        request=request,
    ))


def ajax_compart(request):
    template = loader.get_template("webapp/add_compartment.html")
    compart_number = request.GET.get("compartment")
    return HttpResponse(template.render(
        {"compart_number": compart_number},
        request=request,
    ))


def ajax_device(request):

    current_user = request.user
    device_name = request.GET.get("device_name")
    device_place = request.GET.get("device_place")
    device_type = request.GET.get("device_type")
    compart_number = request.GET.get("compart_nb")
    compart_str = request.GET.get("compart_list")

    compart_list = json.loads(compart_str)

    device_data = {
        "user": current_user,
        "device_name": device_name,
        "device_place": device_place,
        "device_type": device_type,
        "compart_number": compart_number,
        "compart_list": compart_list,
    }

    Sql.device_creation(device_data)

    return redirect(device)
