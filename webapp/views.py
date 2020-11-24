import json
from dal import autocomplete
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from colddeviceapp.models import ColdDevice, ColdDeviceType, Compartment
from prodapp.models import Category, SubCategory, Product, IndustrialProduct
from stockapp.models import Stock
from webapp.sql.db_sql import Sql
from webapp.forms import ProductForm


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
def main_board(request):
    """Product list page"""
    template = loader.get_template("webapp/main_board.html")
    return HttpResponse(template.render(
        request=request,
    ))


def ajax_product_type(request):
    """"""
    template = loader.get_template("webapp/product_type.html")
    return HttpResponse(template.render(request=request))


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
    stocks = Stock.objects.filter(stock_compartment=compartment)
    print(stocks)
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
    get_compartment = request.GET.get("compartment")
    get_product = request.GET.get("product")
    get_subcategory = request.GET.get("subcategory")
    product = Product.objects.get(id=get_product)
    compartment = Compartment.objects.get(id=get_compartment)
    subcategory = SubCategory.objects.get(id=get_subcategory)
    return HttpResponse(template.render(
        {
            "product": product,
            "subcategory": subcategory,
            "compartment": compartment,
        },
        request=request,
    ))



def ajax_stocked(request):
    """"""
    get_compartment = request.GET.get("compartment")
    get_product = request.GET.get("product_name")
    get_product_quantity = request.GET.get("product_quantity")
    get_subcategory = request.GET.get("subcategory")
    subcategory = SubCategory.objects.get(id=get_subcategory)
    compartment = Compartment.objects.get(id=get_compartment)
    product = Product.objects.get(id=get_product)

    stock_data = {
        "product": product,
        "product_quantity": get_product_quantity,
        "compartment": compartment,
        "subcategory": subcategory,
    }

    check_compartment = Stock.objects.filter(stock_compartment=compartment)
    check_product = check_compartment.filter(stock_product=product)
    print(check_product)
    if not check_product:
        Sql.stockage(stock_data)
    else:
        print("ça existe déjà")
    pass


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
