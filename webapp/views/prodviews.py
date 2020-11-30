from dal import autocomplete
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from prodapp.models import Category, SubCategory, IndustrialProduct
from webapp.sql.db_sql import Sql
from webapp.forms import ProductForm


@login_required
def manage_products(request):
    """"""
    prodform = ProductForm
    template = loader.get_template("webapp/product/manage_products.html")
    return HttpResponse(template.render(
        {
            "prodform": prodform,
        },
        request=request
    ))


def ajax_category(request):
    """"""
    template = loader.get_template("webapp/product/category.html")
    categories = Category.objects.all().exclude(category_name="industriel")
    return HttpResponse(template.render(
        {
            "categories": categories,
        },
        request=request,
    ))


def ajax_subcategory(request):
    """"""
    template = loader.get_template("webapp/product/subcategory.html")
    get_category = request.GET.get("category")
    category = Category.objects.get(id=get_category)
    subcategories = SubCategory.objects.filter(subcategory_category=category)
    return HttpResponse(template.render(
        {"subcategories": subcategories},
        request=request,
    ))


def ajax_ind_product(request):
    """"""
    template = loader.get_template("webapp/product/ind_product.html")
    form_class = ProductForm
    test_button = IndustrialProduct.objects.get(id=1)
    return HttpResponse(template.render(
        {
            "prodform": form_class,
            "test_button": test_button,
        },
        request=request,
    ))


def ajax_product_creation(request):
    """"""
    template = loader.get_template("webapp/product/product_creation.html")
    get_subcategory = request.GET.get("subcategory")
    checker = request.GET.get("checker")
    try:
        subcategory = SubCategory.objects.get(id=get_subcategory)
    except ValueError:
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