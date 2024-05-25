from django.shortcuts import render

# Create your views here.
def list(request):
    #测试计划列表
    projects = {'计划1', '计划2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'tplans_list.html', context)  # 渲染模板并返回响应

def delete(request):
    #删除测试计划
    pass
    return render(request, 'tplans_delete.html', )  # 渲染模板并返回响应

def details(request):
    #测试计划详情,也是计划内容列表
    pass
    projects = {'计划内容1', '计划内容2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'tplans_details.html', context)  # 渲染模板并返回响应

def details_content(request):
    #测试计划内容
    pass
    return render(request, 'tplans_details_content.html', )  # 渲染模板并返回响应

def details_content_delete(request):
    #测试计划内容删除
    pass
    return render(request, 'tplans_details_content_delete.html', )  # 渲染模板并返回响应