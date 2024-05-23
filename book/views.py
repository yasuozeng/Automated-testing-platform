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

    # return render(request,template_name='book_list.html')
    # return HttpResponse('book列表')

# def list(request,list_id):
#     return HttpResponse(f'{list_id}book列表')

def details(request):
    return HttpResponse('book详情')

def book_list_to_movie_list(request):
    return render(request,template_name='book_list_to_movie_list.html')

