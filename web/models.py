from django.db import models


# 用户表
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)


# 产品
class Product(models.Model):
    pro_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_desc = models.CharField(max_length=128)
    product_er = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)


# 单一接口用例表
class Apis(models.Model):
    api_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    api_name = models.CharField(max_length=100)
    api_url = models.CharField(max_length=200)
    api_param_value = models.CharField(max_length=800)
    REQUEST_METHOD = (
        ('0', 'get'),
        ('1', 'post'),
    )
    api_method = models.CharField(choices=REQUEST_METHOD, default='get', max_length=200)
    api_result = models.CharField(max_length=200)
    api_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# 流程接口用例表
class ApiTest(models.Model):
    api_t_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    api_t_name = models.CharField(max_length=64)
    api_t_desc = models.CharField(max_length=200)
    api_ter = models.CharField(max_length=200)
    api_t_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# 流程接口步骤表
class ApiStep(models.Model):
    api_test = models.ForeignKey(ApiTest, on_delete=models.CASCADE)
    api_s_name = models.CharField(max_length=100)
    api_s_step = models.CharField(max_length=200)
    api_s_url = models.CharField(max_length=800)
    api_s_param_value = models.CharField(max_length=800)
    REQUEST_METHOD = (
        ('0', 'get'),
        ('1', 'post'),
    )
    api_s_method = models.CharField(choices=REQUEST_METHOD, default='get', max_length=200)
    api_s_result = models.CharField(max_length=200)
    api_s_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
