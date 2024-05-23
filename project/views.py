from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.


def list(request):
    # 项目列表
    projects = {'项目1','项目2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'project_list.html', context)  # 渲染模板并返回响应


def add(request):
    # 新增项目
    pass
    # if request.method == 'POST':
    #     project_name = request.POST.get('project_name')  # 获取表单输入的项目名称
    #     # 调用接口函数，这里假设它接受项目名称并返回一些状态信息
    #     response = call_api_to_add_project(project_name)
    #
    #     # 假设接口调用成功，重定向到项目列表页面
    #     if response['status'] == 'success':
    #         return redirect('project_list')  # project_list是你项目列表的URL名称
    #     else:
    #         # 处理错误情况，比如返回错误信息给前端或重定向到错误页面
    #         return JsonResponse({'error': '项目添加失败'}, status=400)
    # else:
    #     # GET请求时，返回一个错误页面或者直接重定向到项目列表，取决于你的设计
    #     return redirect('project_list')

def delete(request):
    # 删除项目
    # 调用删除项目接口
    return render(request, 'project_delete.html')  # 渲染模板并返回响应

def details_list(request):
    # 项目详情
    projects = ['环境','接口管理','接口用例','业务流程','测试计划','定时任务','测试报告'] # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'project_details_list.html', context)  # 渲染模板并返回响应
