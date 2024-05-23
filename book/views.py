from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template



# Create your views here.


#http://127.0.0.1:8000/book?id=2
def index(request):
    book_id = request.GET.get('id')
    return HttpResponse(f'{book_id}你好')

#http://127.0.0.1:8000/book/2
def index1(request,book_id):
    return HttpResponse(f'{book_id}你好')

def list(request):
    projects = {'项目1','项目2','项目book'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'project_list.html', context)  # 渲染模板并返回响应
    # return render(request, 'book_list.html')  # 渲染模板并返回响应
    # return render(request,template_name='book_list.html')

def details(request):
    return HttpResponse('book详情')

def book_list_to_movie_list(request):
    return render(request,template_name='book_list_to_movie_list.html')

def test(request):
    environment_id = 66
    return render(request, 'test.html', {'environment_id': environment_id})

