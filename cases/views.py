from django.shortcuts import render

# Create your views here.
def interfaces_list(request):
    #接口列表
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