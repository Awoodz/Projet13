import json
from dal import autocomplete
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, SubCategory, Product, IndustrialProduct
from stockapp.models import Stock, Diary, Notification
from webapp.sql.db_sql import Sql
from webapp.forms import ProductForm
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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


def ajax_device_creation(request):
    template = loader.get_template("webapp/create_device.html")
    device_types = ColdDeviceType.objects.all()
    return HttpResponse(template.render(
        {"device_types": device_types},
        request=request,
    ))


def ajax_modify_device(request):
    template = loader.get_template("webapp/modify_device.html")
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
    get_device = request.GET.get("device")
    device_name = request.GET.get("device_name")
    device_place = request.GET.get("device_place")
    device_type = request.GET.get("device_type")
    compart_number = request.GET.get("compart_nb")
    compart_str = request.GET.get("compart_list")

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

    return JsonResponse({"response": "success"})

@login_required
def main_board(request):
    """Product list page"""
    template = loader.get_template("webapp/main_board.html")
    form_class = ProductForm
    return HttpResponse(template.render(
        {
            "prodform": form_class,
        },
        request=request,
    ))


def manage_products(request):
    """"""
    prodform = ProductForm
    template = loader.get_template("webapp/manage_products.html")
    return HttpResponse(template.render(
        {
            "prodform": prodform,
        },
        request=request
    ))


def ajax_category(request):
    """"""
    template = loader.get_template("webapp/category.html")
    categories = Category.objects.all().exclude(category_name="industriel")
    return HttpResponse(template.render(
        {
            "categories": categories,
        },
        request=request,
    ))


def ajax_device(request):
    """"""
    template = loader.get_template("webapp/device.html")
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


def ajax_subcategory(request):
    """"""
    template = loader.get_template("webapp/subcategory.html")
    get_category = request.GET.get("category")
    category = Category.objects.get(id=get_category)
    subcategories = SubCategory.objects.filter(subcategory_category=category)
    return HttpResponse(template.render(
        {"subcategories": subcategories},
        request=request,
    ))


def ajax_ind_product(request):
    """"""
    template = loader.get_template("webapp/ind_product.html")
    form_class = ProductForm
    test_button = IndustrialProduct.objects.get(id=1)
    return HttpResponse(template.render(
        {
            "prodform": form_class,
            "test_button": test_button,
        },
        request=request,
    ))


def ajax_product(request):
    """"""
    template = loader.get_template("webapp/userprod.html")
    current_user = request.user
    products = Product.objects.filter(user_product=current_user)
    return HttpResponse(template.render(
        {
            "products": products,
        },
        request=request,
    ))


def ajax_product_creation(request):
    """"""
    template = loader.get_template("webapp/product_creation.html")
    get_subcategory = request.GET.get("subcategory")
    checker = request.GET.get("checker")
    try:
        subcategory = SubCategory.objects.get(id=get_subcategory)
    except:
        subcategory = get_subcategory
    return HttpResponse(template.render(
        {
            "subcategory": subcategory,
            "checker": checker
        },
        request=request,
    ))


def ajax_create_product(request):
    """"""
    template = loader.get_template("webapp/userprod.html")
    checker = request.GET.get("checker")
    get_subcategory = request.GET.get("subcategory")
    get_product_name = request.GET.get("product_name")
    current_user = request.user

    if checker == "raw":
        product_data = {
            "user": current_user,
            "product_name": get_product_name,
            "subcategory": get_subcategory,
        }
    if checker == "industrial":
        product_data = {
            "user": current_user,
            "product_name": get_product_name,
            "subcategory": "industriel",
        }

    Sql.product_creation(product_data)

    return JsonResponse({"response": "success"})


def ajax_compartment(request):
    """"""
    template = loader.get_template("webapp/compartment.html")
    get_device = request.GET.get("device")
    device = ColdDevice.objects.get(id=get_device)
    compartments = Compartment.objects.filter(compartment_colddevice=device)
    return HttpResponse(template.render(
        {"compartments": compartments},
        request=request,
    ))


def ajax_stock(request):
    """"""
    template = loader.get_template("webapp/stock.html")
    get_compartment = request.GET.get("compartment")
    compartment = Compartment.objects.get(id=get_compartment)
    stocks = Stock.objects.filter(stock_compartment=compartment).exclude(stock_number=0)
    if not stocks:
        return HttpResponse(template.render(request=request))
    else:
        return HttpResponse(template.render(
            {
                "stocks": stocks,
            },
            request=request,
        ))


def ajax_add_to_stock(request):
    """"""
    template = loader.get_template("webapp/add_to_stock.html")
    get_product = request.GET.get("product")
    product = Product.objects.get(id=get_product)
    subcategory = product.product_subcategory
    print(subcategory)
    if subcategory.subcategory_name == "industriel" or subcategory == "autre":
        duration = (
            datetime.now().date() + timedelta(
                days=90
            )
        ).strftime('%d/%m/%Y')
        checker = "nodate"
    else:
        duration = (
            datetime.now().date() + timedelta(
                days=subcategory.subcategory_peremption
            )
        ).strftime('%d/%m/%Y')
        checker = "date"
    
    return HttpResponse(template.render(
        {
            "duration": duration,
            "product": product,
            "checker": checker,
        },
        request=request,
    ))



def ajax_stocked(request):
    """"""
    get_compartment = request.GET.get("compartment")
    get_product = request.GET.get("product")
    get_product_quantity = request.GET.get("product_quantity")
    get_date = request.GET.get("date")
    compartment = Compartment.objects.get(id=get_compartment)
    product = Product.objects.get(id=get_product)
    subcategory = product.product_subcategory

    stock_data = {
        "product": product,
        "product_quantity": get_product_quantity,
        "compartment": compartment,
        "subcategory": subcategory,
        "date": get_date,
    }

    Sql.stockage(stock_data)

    return JsonResponse({"response": "success"})


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    """Autocomplete form"""

    def get_queryset(self):
        """Set how autocomplete form must filter"""

        request = IndustrialProduct.objects.all().order_by("ind_product_name")

        if self.q:
            request = request.filter(
                ind_product_name__istartswith=self.q
            )

        return request


def ajax_remove_stock(request):
    """"""
    get_stock = request.GET.get("stock")
    Sql.remove_stock(get_stock)
    return JsonResponse({"response": "success"})


def emailing(request):
    stocks = Stock.objects.all()
    for stock in stocks:
        if stock.stock_notification.notification_date == datetime.now().date():
            user = stock.stock_compartment.compartment_colddevice.colddevice_user
            product = stock.stock_product.product_name

            subject = "MyColdManager - Rappel"
            html_message = render_to_string(
                "webapp/mail.html",
                {
                    "user": user,
                    "product": product,
                }
            )
            plain_message = strip_tags(html_message)
            from_email = 'From <mycoldmanager@gmail.com>'
            to = user.email

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    return JsonResponse({"response": "success"})