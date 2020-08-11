'''
相关功能：首页，注销
'''
from django.shortcuts import render, redirect
from web.models import Product


# 首页
def home(request):
    pro_count = Product.objects.all().count()

    data = {
        'pro_count': pro_count
    }
    return render(request, 'manage/home_manage.html',context=data)


# 登出
def logout(request):
    request.session.flush()
    return redirect('atp:login')
