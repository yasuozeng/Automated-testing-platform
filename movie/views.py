from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list(request,):
    return HttpResponse('movie列表')

# def list(request,list_id):
#     return HttpResponse(f'{list_id}book列表')

def details(request):
    return HttpResponse('movie详情')