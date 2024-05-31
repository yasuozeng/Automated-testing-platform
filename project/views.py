import logging

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import requests
# Create your views here.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list(request):
    # 项目列表
    # projects = ['项目1','项目2']  # 获取所有项目
    url = "http://localhost:5000/project/project_list"  # 确保这与运行Flask应用的地址和端口匹配
    response = requests.get(url)
    projects=response.json()
    logging.info(f'projects:{projects}')
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'project_list.html', context)  # 渲染模板并返回响应

def add(request):
    # 新增项目
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_name')
        # 在这里处理获取到的项目名称数据，例如保存到数据库中
        url = "http://localhost:5000/project/project_add"
        # 准备要发送的JSON数据
        data = {
            "name": f"{project_name}"
        }
        # 发送POST请求
        requests.post(url, json=data)
        return HttpResponse(f'新增项目成功：{project_name}')
    else:
        # 如果不是 POST 请求，返回空白页面
        return HttpResponse('')


def delete(request):
    # 删除项目
    # 调用删除项目接口
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_delete')
        # 在这里处理获取到的项目名称数据，例如保存到数据库中
        url = "http://localhost:5000/project/project_delete"
        # 准备要发送的JSON数据
        data = {
            "name": f"{project_name}"
        }
        print(f"45646546546465465:::{data}")
        requests.post(url, json=data)
    return render(request, 'project_delete.html')  # 渲染模板并返回响应

def details_list(request):
    # 项目详情
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_datails')
    projects2 = []
    projects2.append(project_name)
    projects = ['环境','接口管理','接口用例','业务流程','测试计划','定时任务','测试报告'] # 获取所有项目
    context = {'projects': projects,'projects2': projects2}  # 创建上下文数据
    return render(request, 'project_details_list.html', context)  # 渲染模板并返回响应
