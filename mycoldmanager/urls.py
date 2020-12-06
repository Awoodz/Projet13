"""mycoldmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
import debug_toolbar
from webapp.views import baseviews as bv
from webapp.views import devviews as dv
from webapp.views import prodviews as pv
from webapp.views import stockviews as sv

urlpatterns = [
    url(r"^$", bv.index, name="index"),
    url(r"^webapp/", include("webapp.urls")),
    url(r"^userapp/", include("userapp.urls")),
    url(r"^create_news/", bv.create_news, name="create_news"),
    url(r"^ajax_create_news/", bv.ajax_create_news, name="ajax_create_news"),
    url(r"^ajax_destroy_news/", bv.ajax_destroy_news, name="ajax_destroy_news"),

    url(r"^manage_devices/", dv.manage_devices, name="manage_devices"),
    url(r"^ajax_device_creation/", dv.ajax_device_creation, name="ajax_device_creation"),
    url(r"^ajax_modify_device/", dv.ajax_modify_device, name="ajax_modify_device"),
    url(r"^ajax_device_modification/", dv.ajax_device_modification, name="ajax_device_modification"),
    url(r"^ajax_compartment_deletion/", dv.ajax_compartment_deletion, name="ajax_compartment_deletion"),
    url(r"^ajax_device_deletion/", dv.ajax_device_deletion, name="ajax_device_deletion"),
    url(r"^ajax_compart/", dv.ajax_compart, name="ajax_compart"),
    url(r"^ajax_create_device/", dv.ajax_create_device, name="ajax_create_device"),
    url(r"^ajax_device/", dv.ajax_device, name="ajax_device"),

    url(r"^manage_products/", pv.manage_products, name="manage_products"),
    url(r"^ajax_category/", pv.ajax_category, name="ajax_category"),
    url(r"^ajax_subcategory/", pv.ajax_subcategory, name="ajax_subcategory"),
    url(r"^product_creation/", pv.ajax_product_creation, name="ajax_product_creation"),
    url(r"^create_product/", pv.ajax_create_product, name="ajax_create_product"),
    url(r"^autocomplete/$", pv.ProductAutocomplete.as_view(), name="autocomplete",),

    url(r"^manage_stocks/", sv.manage_stocks, name="manage_stocks"),
    url(r"^ajax_product/", sv.ajax_product, name="ajax_product"),
    url(r"^ajax_compartment/", sv.ajax_compartment, name="ajax_compartment"),
    url(r"^ajax_stock/", sv.ajax_stock, name="ajax_stock"),
    url(r"^ajax_storage/", sv.ajax_storage, name="ajax_storage"),
    url(r"^ajax_stocked/", sv.ajax_stocked, name="ajax_stocked"),
    url(r"^ajax_remove_stock/", sv.ajax_remove_stock, name="ajax_remove_stock"),

    path('admin/', admin.site.urls),
    path("accounts/", include("userapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
