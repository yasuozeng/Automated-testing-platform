import logging

import requests
from django.shortcuts import render

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create your views here.
def interfaces_list(request):
    #接口列表
    if request.method == 'POST':
        project_name = request.POST.get('project_datails')

    url_all = "http://localhost:5000/intercase/intercase_list"
    # 准备要发送的JSON数据

    data_all = {
        "project_name": f"{project_name}"
    }

    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')

    projects2 = []
    projects2.append(project_name)


    context = {'projects': environment_old_name_list, 'projects2': projects2,'projects3':projects_json_all}  # 创建上下文数据
    return render(request, 'interfaces_update.html', context)  # 渲染模板并返回响应


    projects = {'接口1', '接口2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'cases_interfaces_list.html', context)  # 渲染模板并返回响应

def list(request):
    #接口用例列表
    projects = {'接口用例1', '接口用例2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'cases_list.html', context)  # 渲染模板并返回响应

def details(request):
    # 接口用例详情
    cases = 55  # 获取所有项目
    cases_api='/user/login'
    context = {'cases_id': cases,'cases_api':cases_api}  # 创建上下文数据
    return render(request, 'cases_details.html', context=context)  # 渲染模板并返回响应

def delete(request):
    # 删除接口用例
    return render(request, 'cases_delete.html', )  # 渲染模板并返回响应

def add(request):
    # 新增接口用例
    return render(request, 'cases_add.html', )  # 渲染模板并返回响应