'''
相关功能：webUI的增删改查
'''
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from web.models import Product


# webUI列表
def web_test_manage(request):
    return render(request, 'web/web_test_manage.html')
