from django.shortcuts import render

# Create your views here.
def list(request):
    #定时任务列表
    projects = {'定时任务1', '定时任务2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'tasks_list.html', context)  # 渲染模板并返回响应

def delete(request):
    #删除定时任务
    pass
    return render(request, 'tasks_delete.html', )  # 渲染模板并返回响应

def details(request):
    #定时任务详情,也是定时任务内容列表
    pass
    projects = {'定时任务内容1', '定时任务内容2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'tasks_details.html', context)  # 渲染模板并返回响应

def content_details(request):
    #定时任务内容
    pass
    return render(request, 'tasks_details_content.html', )  # 渲染模板并返回响应

def content_delete(request):
    #定时任务内容删除
    pass
    return render(request, 'tasks_details_content_delete.html', )  # 渲染模板并返回响应