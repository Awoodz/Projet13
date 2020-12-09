import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template import loader

from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from webapp.sql.db_sql import Sql


@login_required
def manage_devices(request):
    """"""
    template = loader.get_template("webapp/device/manage_devices.html")
    return HttpResponse(template.render(request=request))


def ajax_device_creation(request):
    template = loader.get_template("webapp/device/create_device.html")
    device_types = ColdDeviceType.objects.all()
    return HttpResponse(template.render(
        {"device_types": device_types},
        request=request,
    ))


def ajax_modify_device(request):
    template = loader.get_template("webapp/device/modify_device.html")
    get_device = request.GET.get("device")
    device = ColdDevice.objects.get(pk=get_device)
    compartments = Compartment.objects.filter(compartment_colddevice=device)
    device_types = ColdDeviceType.objects.all()
    return HttpResponse(template.render(
        {
            "device": device,
            "compartments": compartments,
            "device_types": device_types,
        },
        request=request,
    ))


def ajax_device_modification(request):
    # get_device = request.GET.get("device")
    # device_name = request.GET.get("device_name")
    # device_place = request.GET.get("device_place")
    # device_type = request.GET.get("device_type")
    # compart_number = request.GET.get("compart_nb")
    # compart_str = request.GET.get("compart_list")

    return JsonResponse({"response": "success"})


def ajax_compartment_deletion(request):
    get_compartment = request.GET.get("compartment")
    Sql.remove_compartment(get_compartment)
    return JsonResponse({"response": "success"})


def ajax_device_deletion(request):
    get_device = request.GET.get("device")
    Sql.remove_device(get_device)
    return JsonResponse({"response": "success"})


def ajax_compart(request):
    template = loader.get_template("webapp/device/add_compartment.html")
    compart_number = request.GET.get("compartment")
    return HttpResponse(template.render(
        {"compart_number": compart_number},
        request=request,
    ))


def ajax_create_device(request):
    """"""
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

    return JsonResponse({"response": "success"})


def ajax_device(request):
    """"""
    template = loader.get_template("webapp/device/device.html")
    checker = request.GET.get("checker")
    current_user = request.user
    user_devices = ColdDevice.objects.filter(colddevice_user=current_user.id)
    return HttpResponse(template.render(
        {
            "checker": checker,
            "user_devices": user_devices,
        },
        request=request,
    ))
