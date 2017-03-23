"""semi_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^new$', views.new, name = "new"),
    url(r'^create$', views.create, name = "create"),
    url(r'^(?P<product_id>\d+)/show$', views.show, name = "show"),
    url(r'^(?P<product_id>\d+)/edit$', views.edit, name = "edit"),
    url(r'^(?P<product_id>\d+)/update$', views.update, name = "update"),
    url(r'^(?P<product_id>\d+)/destroy$', views.destroy, name = "destroy"),
]
