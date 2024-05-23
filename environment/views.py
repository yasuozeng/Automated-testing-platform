from django.shortcuts import render

# Create your views here.
def list(request):
    #环境列表
    projects = {'环境1','环境2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'list.html', context)  # 渲染模板并返回响应

def details(request):
    pass

def delete(request):
    pass

def update(request):
    pass