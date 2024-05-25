"""
URL configuration for djangoa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.shortcuts import render
from django.template import Template
app_name = 'processes'#业务流程
urlpatterns = [
    path('flow/list', views.flow_list,name='flow_list'),
    path('flow/delete', views.flow_delete,name='flow_delete'),
    path('flow/details', views.flow_details,name='flow_details'),
    path('flow/details/addstep', views.addstep,name='addstep'),
    path('flow/details/deletestep', views.deletestep,name='deletestep'),
    path('flow/details/detailsstep', views.detailsstep,name='detailsstep'),
    # path('list', views.list,name='list'),

]
