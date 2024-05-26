from django.shortcuts import render
import requests

# Create your views here.
def list(request):
    #环境列表
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中的数据
        project_name = request.POST.get('project_name')
    # 在这里处理获取到的项目名称数据，例如保存到数据库中
    url = "http://localhost:5000/project/project_delete"
    # 准备要发送的JSON数据
    data = {
        "name": f"{project_name}"
    }

    projects = requests.post(url, json=data)
    # projects = {'环境1','环境2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'list.html', context)  # 渲染模板并返回响应
    # return render(request, 'book_list.html')  # 渲染模板并返回响应

def details(request):
    # 环境详情
    environment_id = 66
    return render(request, 'details.html', {'environment_id': environment_id})
    # pass

def delete(request):
    # 删除环境
    return render(request, 'delete.html', )

def update(request):
    pass