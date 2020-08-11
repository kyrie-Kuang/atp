'''
相关功能：单一接口的增删改查
'''
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from web.models import Apis, Product


# 单一接口列表
def apis_manage(request):
    apis_list = Apis.objects.all()

    paginator = Paginator(apis_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'apis_list': page_object,
    }
    return render(request, 'apis/apis_manage.html', context=data)


# 单一接口添加
def apis_add(request):
    pro_names = Product.objects.all()

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
        }
        return render(request, 'apis/apis_add.html', context=data)

    elif request.method == "POST":

        api_product = request.POST.get('dropdown')
        api_name = request.POST.get('api_name')
        api_url = request.POST.get('api_url')
        api_param_value = request.POST.get('api_param_value')
        api_method = request.POST.get('method_check')
        api_result = request.POST.get('api_result')
        api_status = request.POST.get('api_status')

        Apis.objects.create(
            api_name=api_name,
            api_url=api_url,
            api_param_value=api_param_value,
            api_method=api_method,
            api_result=api_result,
            api_status=api_status,
            api_product_id=api_product,
        )
        return redirect('atp:apis_manage')


# 单一接口删除
def apis_delete(request):
    apis_id = request.GET['apis_id']
    try:
        apis_obj = Apis.objects.get(id=apis_id)
        apis_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 单一接口编辑
def apis_update(request, apis_id):
    pro_names = Product.objects.all()
    apis = Apis.objects.get(id=apis_id)

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
            'apis': apis,
        }
        return render(request, 'apis/apis_update.html', context=data)
    elif request.method == "POST":
        api_product = request.POST.get('dropdown')
        api_name = request.POST.get('api_name')
        api_url = request.POST.get('api_url')
        api_param_value = request.POST.get('api_param_value')
        api_method = request.POST.get('method_check')
        api_result = request.POST.get('api_result')
        api_status = request.POST.get('api_status')

        Apis.objects.filter(id=apis_id).update(
            api_name=api_name,
            api_url=api_url,
            api_param_value=api_param_value,
            api_method=api_method,
            api_result=api_result,
            api_status=api_status,
            api_product_id=api_product
        )

        return redirect('atp:apis_manage')


# 单一接口搜索
def apis_search(request):
    search_name = request.GET.get('apis_name')
    api_list = Apis.objects.filter(api_name__icontains=search_name)

    paginator = Paginator(api_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    apis_lists = paginator.page(page)

    data = {
        "apis_list": apis_lists,
    }
    return render(request, 'apis/apis_manage.html', context=data)
