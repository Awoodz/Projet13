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
    url(r"^create_device/", webviews.create_device, name="create_device"),
    url(r"^ajax_compart/", webviews.ajax_compart, name="ajax_compart"),
    path('admin/', admin.site.urls),
    path("accounts/", include("userapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
