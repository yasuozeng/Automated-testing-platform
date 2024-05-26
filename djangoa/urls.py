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
import requests
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from book import views
from django.http import HttpResponse
from django.template import Template

def index(request):
    # 项目列表
    # projects = ['项目1','项目2']  # 获取所有项目
    url = "http://localhost:5000/project/project_list"  # 确保这与运行Flask应用的地址和端口匹配
    response = requests.get(url)
    projects=response.json()
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'project_list.html', context)  # 渲染模板并返回响应

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('book/',include('book.urls'),name='book'),
    path('movie/',include('movie.urls'),name='movie'),
    path('project/',include('project.urls'),name='project'),
    path('environment/',include('environment.urls'),name='environment'),
    path('tplans/',include('tplans.urls'),name='tplans'),
    path('interfaces/',include('interfaces.urls'),name='interfaces'),
    path('cases/',include('cases.urls'),name='cases'),
    path('processes/',include('processes.urls'),name='processes'),
    path('tasks/',include('tasks.urls'),name='tasks'),
    path('reports/',include('reports.urls'),name='reports'),
]
