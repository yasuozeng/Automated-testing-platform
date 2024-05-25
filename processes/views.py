from django.shortcuts import render

# Create your views here.
def flow_list(request):
    # 业务流程flow列表
    projects = {'业务流程1', '业务流程2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'processes_flow_list.html', context)  # 渲染模板并返回响应

def flow_delete(request):
    # 业务流程删除
    pass
    return render(request, 'processes_delete.html',)  # 渲染模板并返回响应

def flow_details(request):
    # 业务流程详情,也是业务步骤列表
    pass
    projects = {'业务步骤1', '业务步骤2'}  # 获取所有项目
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'processes_flow_details.html',context)  # 渲染模板并返回响应

def addstep(request):
    # 业务步骤新增
    pass
    return render(request, 'processes_flow_list.html', )  # 渲染模板并返回响应

def deletestep(request):
    # 业务步骤删除
    pass
    return render(request, 'processes_deletestep.html', )  # 渲染模板并返回响应

def detailsstep(request):
    # 业务步骤详情
    projects = {'业务步骤详情1', '业务步骤详情2'}  # 获取所有接口用例
    context = {'projects': projects}  # 创建上下文数据
    return render(request, 'processes_detailsstep.html', context)  # 渲染模板并返回响应