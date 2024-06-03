import logging

import requests
from django.shortcuts import render

# Create your views here.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def list(request):
    # 接口列表
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')

        url = "http://localhost:5000/interface/interface_list"
        # 准备要发送的JSON数据
        data = {
            "project_name": f"{project_name}"
        }

        logging.info(f'data:{data}')

        # 发送POST请求
        response = requests.post(url, json=data)

        # 确保响应的编码为 UTF-8
        response.encoding = 'utf-8'

        # 将响应内容解析为 JSON
        projects_json = response.json()

        logging.info(f'projects_json:{projects_json}')

        # 提取接口名称列表
        interface_name_list = [entry[2] for entry in projects_json]

        logging.info(f"interface_name_list:{interface_name_list}")

        # 创建项目名称列表
        projects2 = [project_name]

        logging.info(f'projects2:{projects2}')
        logging.info(f'projects:{response}')
        logging.info(f'projects_text:{response.text}')

        # 创建上下文数据
        context = {
            'projects': interface_name_list,
            'projects2': projects2
        }

        # 渲染模板并返回响应
        return render(request, 'interfaces_list.html', context=context)

    # 如果不是 POST 请求，返回一些默认值或处理其他方法
    return render(request, 'interfaces_list.html', context={})

def details(request):
    # 接口详情
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        interface_old_name = request.POST.get('interface_old_name')

    logging.info(f'project_name:{project_name}')
    logging.info(f'interface_old_name:{interface_old_name}')

    url_all = "http://localhost:5000/interface/interface_details"
    data_all = {
        "project_name": f"{project_name}",
        "name": f'{interface_old_name}',
    }

    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')
    interface_name=projects_json_all[0][2]
    interface_url = projects_json_all[0][3]
    interface_method = projects_json_all[0][4]
    interface_type = projects_json_all[0][5]

    interface_name_list=[]
    interface_name_list.append(interface_name)

    interface_url_list=[]
    interface_url_list.append(interface_url)

    interface_method_list=[]
    interface_method_list.append(interface_method)

    interface_type_list=[]
    interface_type_list.append(interface_type)

    logging.info(f'interface_name_list:{interface_name_list},interface_url_list:{interface_url_list},'
                 f'interface_method_list:{interface_method_list},interface_type_list:{interface_type_list},')

    projects2 = []
    projects2.append(project_name)
    environment_old_name_list = []
    environment_old_name_list.append(interface_old_name)

    context = {'interface_name_list': interface_name_list, 'projects2': projects2,'interface_url_list':interface_url_list
               ,'interface_method_list':interface_method_list,'interface_type_list':interface_type_list}  # 创建上下文数据
    return render(request, 'interfaces_details.html', context)  # 渲染模板并返回响应


def delete(request):
    # 删除接口
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        interface_name = request.POST.get('interface_name')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/interface/interface_delete"
    # 准备要发送的JSON数据
    data = {
        "name": f"{interface_name}",
        "project_name": f"{project_name}"
    }
    logging.info(f'data:{data}')
    projects = requests.post(url, json=data)
    projects_json = projects.json()
    projects2 = []
    projects2.append(project_name)
    context = {'projects': projects_json,'projects2': projects2}  # 创建上下文数据
    return render(request, 'interfaces_delete.html',context )



    return render(request, 'interfaces_delete.html', )  # 渲染模板并返回响应

def add(request):
    # 新增接口
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        environment_name = request.POST.get('interface_name')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/interface/interface_add"
    # 准备要发送的JSON数据
    data = {
        "project_name": f"{project_name}",
        "name": f"{environment_name}",
    }
    logging.info(f'data:{data}')
    projects = requests.post(url, json=data)
    projects_json = projects.json()
    projects2 = []
    projects2.append(project_name)
    context = {'projects': projects_json,'projects2': projects2}  # 创建上下文数据
    return render(request, 'interfaces_add.html',context)  # 渲染模板并返回响应








    return render(request, 'interfaces_add.html', )  # 渲染模板并返回响应

def update(request):
    # 接口详情
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
        interface_new_name = request.POST.get('interface_new_name')
        interface_old_name = request.POST.get('interface_old_name')
        interface_url = request.POST.get('interface_url')
        interface_type = request.POST.get('interface_type')
        interface_method = request.POST.get('interface_method')

    logging.info(f'project_name:{project_name}')
    logging.info(f'interface_old_name:{interface_old_name}')



    url_all = "http://localhost:5000/interface/interface_update"
    # 准备要发送的JSON数据

    data_all = {
        "project_name": f"{project_name}",
        "name": f'{interface_new_name}',
        "url": f'{interface_url}',
        "method": f'{interface_method}',
        "type": f'{interface_type}',
        "interface_old_name": f'{interface_old_name}'
    }

    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')


    projects2 = []
    projects2.append(project_name)
    environment_old_name_list = []
    environment_old_name_list.append(interface_old_name)

    context = {'projects': environment_old_name_list, 'projects2': projects2,'projects3':projects_json_all}  # 创建上下文数据
    return render(request, 'interfaces_update.html', context)  # 渲染模板并返回响应