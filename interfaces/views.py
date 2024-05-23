from django.shortcuts import render

# Create your views here.

def list(request):
    # 接口列表
    projects = ['接口管理1', '接口管理2']  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request,'interfaces_list.html', context=context)  # 渲染模板并返回响应

def details(request):
    # 接口详情
    interfaces = 55  # 获取所有项目
    context = {'interfaces_id': interfaces}  # 创建上下文数据
    return render(request, 'interfaces_details.html', context=context)  # 渲染模板并返回响应

def delete(request):
    # 删除接口
    return render(request, 'interfaces_delete.html', )  # 渲染模板并返回响应