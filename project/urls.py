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
app_name='project'
urlpatterns = [
    path('list', views.list,name='project_list'),
    path('add', views.add,name='project_add'),
    path('details', views.details_list,name='project_details_list'),
    path('delete', views.delete,name='project_delete'),
    # path('add', views.delete,name='project_delete'),
]
