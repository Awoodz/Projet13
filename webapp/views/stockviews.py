
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from colddeviceapp.models import ColdDevice, Compartment
from prodapp.models import Product
from stockapp.models import Stock
from webapp.sql.db_sql import Sql


@login_required
def manage_stocks(request):
    """"""
    template = loader.get_template("webapp/stock/manage_stocks.html")
    return HttpResponse(template.render(request=request))


def ajax_product(request):
    """"""
    template = loader.get_template("webapp/stock/userprod.html")
    current_user = request.user
    products = Product.objects.filter(user_product=current_user)
    return HttpResponse(template.render(
        {
            "products": products,
        },
        request=request,
    ))


def ajax_compartment(request):
    """"""
    template = loader.get_template("webapp/stock/compartment.html")
    get_device = request.GET.get("device")
    device = ColdDevice.objects.get(id=get_device)
    compartments = Compartment.objects.filter(compartment_colddevice=device)
    return HttpResponse(template.render(
        {"compartments": compartments},
        request=request,
    ))


def ajax_stock(request):
    """"""
    template = loader.get_template("webapp/stock/stock.html")
    get_compartment = request.GET.get("compartment")
    compartment = Compartment.objects.get(id=get_compartment)
    stocks = Stock.objects.filter(
        stock_compartment=compartment
    ).exclude(stock_number__lte=0)
    if not stocks:
        return HttpResponse(template.render(request=request))
    else:
        return HttpResponse(template.render(
            {
                "stocks": stocks,
            },
            request=request,
        ))


def ajax_storage(request):
    """"""
    template = loader.get_template("webapp/stock/storage.html")
    get_product = request.GET.get("product")
    product = Product.objects.get(id=get_product)
    subcategory = product.product_subcategory
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
    print(get_compartment, get_product, get_product_quantity, get_date)

    stock_data = {
        "product": product,
        "product_quantity": get_product_quantity,
        "compartment": compartment,
        "subcategory": subcategory,
        "date": get_date,
    }

    Sql.stockage(stock_data)

    return JsonResponse({"response": "success"})


def ajax_remove_stock(request):
    """"""
    get_stock = request.GET.get("stock")
    Sql.remove_stock(get_stock)
    return JsonResponse({"response": "success"})
