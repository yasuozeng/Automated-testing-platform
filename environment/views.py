from django.shortcuts import render

# Create your views here.
def list(request):
    #环境列表
    projects = {'环境1','环境2'}  # 获取所有项目
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