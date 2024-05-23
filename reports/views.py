from django.shortcuts import render

# Create your views here.
def list(request):
    def list(request):
        projects = {'测试报告1', '测试报告2'}  # 获取所有项目
        context = {'projects': projects}  # 创建上下文数据
        return render(request, 'list.html', context)  # 渲染模板并返回响应