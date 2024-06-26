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
app_name = 'cases'#接口用例
urlpatterns = [
    path('list', views.list,name='list'),
    path('interfaces', views.interfaces_list,name='interfaces'),
    path('details', views.details,name='details'),
    path('delete', views.delete,name='delete'),
    path('add', views.add,name='add'),
    path('update', views.update, name='update'),
]
