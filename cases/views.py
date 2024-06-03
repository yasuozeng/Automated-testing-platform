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


    context = {'projects2': projects2,'projects3':projects_json_all}  # 创建上下文数据
    return render(request, 'interfaces_update.html', context)  # 渲染模板并返回响应


    projects = {'接口1', '接口2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'cases_interfaces_list.html', context)  # 渲染模板并返回响应

def list(request):
    #接口用例列表
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

    cases_name_list = [entry[2] for entry in projects_json_all]
    logging.info(f"interface_name_list:{cases_name_list}")

    projects2 = []
    projects2.append(project_name)

    context = {'projects2': projects2,'cases_name_list':cases_name_list}  # 创建上下文数据
    return render(request, 'cases_list.html', context)  # 渲染模板并返回响应



def details(request):
    # 接口用例详情
    if request.method == 'POST':
        project_name = request.POST.get('project_datails')
        old_title = request.POST.get('old_title')
    url_all = "http://localhost:5000/intercase/intercase_details"
    # 准备要发送的JSON数据

    data_all = {
        "project_name": f"{project_name}",
        "old_title": f"{old_title}"

    }

    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')

    new_title = projects_json_all[0][2]
    interfaes_id = projects_json_all[0][3]
    headers = projects_json_all[0][4]
    case_request = projects_json_all[0][5]
    case_file = projects_json_all[0][6]
    case_setup_script = projects_json_all[0][7]
    case_teardown_script = projects_json_all[0][8]

    old_title_list=[]
    old_title_list.append(old_title)

    interfaes_id_list=[]
    interfaes_id_list.append(interfaes_id)

    headers_list=[]
    headers_list.append(headers)

    case_request_list=[]
    case_request_list.append(case_request)

    case_file_list=[]
    case_file_list.append(case_file)

    case_setup_script_list=[]
    case_setup_script_list.append(case_setup_script)

    case_teardown_script_list=[]
    case_teardown_script_list.append(case_teardown_script)

    projects2 = []
    projects2.append(project_name)

    context = {'projects2': projects2,'old_title_list':old_title_list,'interfaes_id_list':interfaes_id_list,
               'headers_list':headers_list,'case_request_list':case_request_list,'case_file_list':case_file_list,
               'case_setup_script_list':case_setup_script_list,'case_teardown_script_list':case_teardown_script_list}  # 创建上下文数据
    return render(request, 'cases_details.html', context)  # 渲染模板并返回响应

def update(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_datails')
        old_title = request.POST.get('old_title')


    data = {
        "project_name": "自动化测试平台",
        'interface':2,
        "title": "1",
        "headers": {"Content-Type": "application/json"},
        "request": {"name": "1test项目新增"},
        "file": {"": ""},
        "setup_script": "",
        "teardown_script": "",
        "title": "2"
    }

    return render(request, 'cases_details.html')  # 渲染模板并返回响应




def delete(request):
    # 删除接口用例
    if request.method == 'POST':
        cases_name = request.POST.get('cases_name')
        project_name = request.POST.get('project_datails')

    url_all = "http://localhost:5000/intercase/intercase_delete"
    # 准备要发送的JSON数据

    data_all = {
        "title": f"{cases_name}"
    }

    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')

    projects2 = []
    projects2.append(project_name)

    context = {'projects2': projects2}  # 创建上下文数据
    return render(request, 'cases_delete.html', context)  # 渲染模板并返回响应

def add(request):
    # 新增接口用例
    if request.method == 'POST':
        project_name = request.POST.get('project_datails')
        cases_old_name = request.POST.get('caces_name')
    url_all = "http://localhost:5000/intercase/intercase_add"
    # 准备要发送的JSON数据

    data_all = {
        "project_name": f"{project_name}",
        'title':f'{cases_old_name}'
    }

    logging.info(f'data_all:{data_all}')
    projects_all = requests.post(url_all, json=data_all)
    projects_json_all = projects_all.json()
    logging.info(f'projects_json_all:{projects_json_all}')

    projects2 = []
    projects2.append(project_name)

    context = {'projects2': projects2}  # 创建上下文数据
    return render(request, 'cases_add.html', context)  # 渲染模板并返回响应
