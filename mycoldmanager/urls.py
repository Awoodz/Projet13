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
from webapp import views as webviews

urlpatterns = [
    url(r"^$", webviews.index, name="index"),
    url(r"^webapp/", include("webapp.urls")),
    url(r"^userapp/", include("userapp.urls")),
    url(r"^device/", webviews.device, name="device"),
    url(r"^ajax_device_creation/", webviews.ajax_device_creation, name="ajax_device_creation"),
    url(r"^ajax_compart/", webviews.ajax_compart, name="ajax_compart"),
    url(r"^ajax_create_device/", webviews.ajax_create_device, name="ajax_create_device"),
    url(r"^ajax_modify_device/", webviews.ajax_modify_device, name="ajax_modify_device"),
    url(r"^ajax_device_modification/", webviews.ajax_device_modification, name="ajax_device_modification"),
    url(r"^ajax_device_deletion/", webviews.ajax_device_deletion, name="ajax_device_deletion"),
    url(r"^ajax_compartment_deletion/", webviews.ajax_compartment_deletion, name="ajax_compartment_deletion"),
    url(r"^ajax_subcategory/", webviews.ajax_subcategory, name="ajax_subcategory"),
    url(r"^ajax_product/", webviews.ajax_product, name="ajax_product"),
    url(r"^manage_products/", webviews.manage_products, name="manage_products"),
    url(r"^manage_devices/", webviews.manage_devices, name="manage_devices"),
    url(r"^manage_stocks/", webviews.manage_stocks, name="manage_stocks"),
    url(r"^ajax_device/", webviews.ajax_device, name="ajax_device"),
    url(r"^ajax_category/", webviews.ajax_category, name="ajax_category"),
    url(r"^ajax_ind_product/", webviews.ajax_ind_product, name="ajax_ind_product"),
    url(r"^product_creation/", webviews.ajax_product_creation, name="ajax_product_creation"),
    url(r"^create_product/", webviews.ajax_create_product, name="ajax_create_product"),
    url(r"^ajax_compartment/", webviews.ajax_compartment, name="ajax_compartment"),
    url(r"^ajax_stock/", webviews.ajax_stock, name="ajax_stock"),
    url(r"^ajax_storage/", webviews.ajax_storage, name="ajax_storage"),
    url(r"^ajax_stocked/", webviews.ajax_stocked, name="ajax_stocked"),
    url(r"^ajax_remove_stock/", webviews.ajax_remove_stock, name="ajax_remove_stock"),
    url(r"^autocomplete/$", webviews.ProductAutocomplete.as_view(), name="autocomplete",),
    path('admin/', admin.site.urls),
    path("accounts/", include("userapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
