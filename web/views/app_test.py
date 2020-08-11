'''
相关功能：appUI的增删改查
'''
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from web.models import Product


# appUI列表
def app_test_manage(request):
    return render(request, 'app/app_test_manage.html')
