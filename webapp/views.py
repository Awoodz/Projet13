import json
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, SubCategory, Product
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


def ajax_create_device(request):

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

@login_required
def product(request):
    """Product list page"""
    template = loader.get_template("webapp/product.html")
    current_user = request.user
    user_devices = ColdDevice.objects.filter(colddevice_user=current_user.id)
    categories = Category.objects.all()
    return HttpResponse(template.render(
        {
            "categories": categories,
            "user_devices": user_devices,
        },
        request=request,
    ))


def ajax_subcategory(request):
    """"""
    template = loader.get_template("webapp/subcategory.html")
    get_category = request.GET.get("category")
    print(get_category)
    category = Category.objects.get(category_name=get_category)
    subcategories = SubCategory.objects.filter(subcategory_category=category)
    return HttpResponse(template.render(
        {"subcategories": subcategories},
        request=request,
    ))


def ajax_product(request):
    """"""
    template = loader.get_template("webapp/userprod.html")
    get_subcategory = request.GET.get("subcategory")
    subcategory = SubCategory.objects.get(subcategory_name=get_subcategory)
    current_user = request.user
    user_products = Product.objects.filter(user_product=current_user)
    products = user_products.filter(product_subcategory=subcategory)
    return HttpResponse(template.render(
        {
            "products": products,
            "subcategory": subcategory
        },
        request=request,
    ))


def ajax_product_creation(request):
    """"""
    template = loader.get_template("webapp/product_creation.html")
    get_subcategory = request.GET.get("subcategory")
    subcategory = SubCategory.objects.get(subcategory_name=get_subcategory)
    return HttpResponse(template.render(
        {"subcategory": subcategory},
        request=request,
    ))


def ajax_create_product(request):
    """"""
    template = loader.get_template("webapp/userprod.html")
    get_subcategory = request.GET.get("subcategory")
    get_product_name = request.GET.get("product_name")
    current_user = request.user

    product_data = {
        "user": current_user,
        "product_name": get_product_name,
        "subcategory": get_subcategory,
    }

    Sql.product_creation(product_data)

    subcategory = SubCategory.objects.get(subcategory_name=get_subcategory)
    user_products = Product.objects.filter(user_product=current_user)
    products = user_products.filter(product_subcategory=subcategory)

    return HttpResponse(template.render(
        {
            "products": products,
            "subcategory": subcategory,
        },
        request=request,
    ))


def ajax_device(request):
    """"""
    template = loader.get_template("webapp/compartment.html")
    get_device = request.GET.get("device")
    device = ColdDevice.objects.get(colddevice_name=get_device)
    compartments = Compartment.objects.filter(compartment_colddevice=device)
    return HttpResponse(template.render(
        {"compartments": compartments},
        request=request,
    ))
