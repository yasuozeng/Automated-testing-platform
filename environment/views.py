import json
import logging

from django.shortcuts import render
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Create your views here.
def list(request):
    #环境列表
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/environment/environment_name_list"
    # 准备要发送的JSON数据
    data = {
        "name": f"{project_name}"
    }
    logging.info(f'data:{data}')
    projects = requests.post(url, json=data)
    projects_json = projects.json()

    projects2 = []
    projects2.append(project_name)
    logging.info(f'projects2:{projects2}')
    logging.info(f'projects:{projects}')
    logging.info(f'projects_text:{projects.text}')
    logging.info(f'projects_json:{projects_json}')
    context = {'projects': projects_json,'projects2': projects2}  # 创建上下文数据
    return render(request, 'list.html', context)  # 渲染模板并返回响应

def details(request):
    # 环境详情
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        environment_old_name = request.POST.get('environment_old_name')

    logging.info(f'project_name:{project_name}')
    logging.info(f'environment_old_name:{environment_old_name}')

    url_all = "http://localhost:5000/environment/environment_list"
    # 准备要发送的JSON数据
    data_all = {
        "name": f"{project_name}",
        'environment_name':f'{environment_old_name}'
    }
    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')
    environment_host=projects_json_all[0][6]

    environment_host_list=[]
    environment_host_list.append(environment_host)

    logging.info(f'environment_host:{environment_host}')
    projects2 = []
    projects2.append(project_name)
    environment_old_name_list = []
    environment_old_name_list.append(environment_old_name)
    context = {'projects': environment_old_name_list, 'projects2': projects2,'projects3':projects_json_all
               ,'projects4':environment_host_list}  # 创建上下文数据
    return render(request, 'details.html', context)  # 渲染模板并返回响应


def delete(request):
    # 删除环境
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        environment_name = request.POST.get('environment_name')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/environment/environment_delete"
    # 准备要发送的JSON数据
    data = {
        "environment_name": f"{environment_name}",
        "project_name": f"{project_name}"
    }
    logging.info(f'data:{data}')
    projects = requests.post(url, json=data)
    projects_json = projects.json()
    projects2 = []
    projects2.append(project_name)
    context = {'projects': projects_json,'projects2': projects2}  # 创建上下文数据
    return render(request, 'delete.html',context )

def update(request):
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        environment_old_name = request.POST.get('environment_old_name')
        environment_new_name = request.POST.get('environment_new_name')
        host = request.POST.get('host')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/environment/environment_update"
    # 准备要发送的JSON数据
    data = {

        'environment_old_name': f'{environment_old_name}',
        'environment_new_name': f'{environment_new_name}',
        'project_name': f'{project_name}',
        'host': f'{host}'
    }
    logging.info(f'data:{data}')
    projects = requests.post(url, json=data)
    projects_json = projects.json()
    projects2 = []
    projects2.append(project_name)
    context = {'projects': projects_json,'projects2': projects2}  # 创建上下文数据
    return render(request, 'update.html',context)  # 渲染模板并返回响应



def base(request):
    return render(request, 'base.html' )

def bootstrap(request):
    return render(request, 'bootstrap.html' )

def add(request):
    #新增环境
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        environment_name = request.POST.get('environment_name')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/environment//environment_add"
    # 准备要发送的JSON数据
    data = {
        "environment_name": f"{environment_name}",
        "project_name": f"{project_name}",
    }
    logging.info(f'data:{data}')
    projects = requests.post(url, json=data)
    projects_json = projects.json()
    projects2 = []
    projects2.append(project_name)
    context = {'projects': projects_json,'projects2': projects2}  # 创建上下文数据
    return render(request, 'add.html',context)  # 渲染模板并返回响应
