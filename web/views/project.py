'''
相关功能：产品的增删改查功能
'''
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from web.models import Product


# 产品列表
def product_manage(request):
    products = Product.objects.all()

    paginator = Paginator(products, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    pro_lists = paginator.page(page)

    data = {
        'products': pro_lists,
    }
    return render(request, 'product/product_manage.html', context=data)


# 产品添加
def product_add(request):
    user_id = request.session.get('user_id')

    if request.method == "GET":
        return render(request, 'product/product_add.html')
    elif request.method == "POST":
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        product_er = request.POST.get('product_er')

        pro_obj = Product.objects.filter(product_name=product_name)
        if pro_obj.exists():
            data = {
                'msg_pro_name': '产品已存在'
            }
            return render(request, 'product/product_add.html', context=data)
        else:
            Product.objects.create(
                product_name=product_name,
                product_desc=product_desc,
                product_er=product_er,
                pro_user_id=user_id,
            )
        return redirect('atp:product_manage')


# 产品删除
def product_delete(request):
    product_id = request.GET['product_id']
    try:
        pro_obj = Product.objects.get(id=product_id)
        pro_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 200})


# 产品编辑
def product_update(request, pro_id):
    pro_obj = Product.objects.get(id=pro_id)

    if request.method == "GET":
        data = {
            'pro_obj': pro_obj,
        }
        return render(request, 'product/product_update.html', context=data)
    elif request.method == "POST":
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        product_er = request.POST.get('product_er')

        pro = Product.objects.filter(product_name=product_name)

        if pro.exists() and pro_obj.product_name != product_name:
            data = {
                'pro_obj': pro_obj,
                'msg_pro_name': '产品已存在'
            }
            return render(request, 'product/product_update.html', context=data)
        else:
            Product.objects.filter(id=pro_id).update(
                product_name=product_name,
                product_desc=product_desc,
                product_er=product_er
            )

            return redirect('atp:product_manage')


# 产品搜索
def product_search(request, ):
    search_name = request.GET.get('product_name')
    pro_list = Product.objects.filter(product_name__icontains=search_name)

    paginator = Paginator(pro_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    pro_lists = paginator.page(page)

    data = {
        "products": pro_lists,
    }
    return render(request, 'product/product_manage.html', context=data)
