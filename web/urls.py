from django.urls import path
from web.views import account, manage, project, apis, api_test, web_test, app_test

urlpatterns = [
    # 登录注册
    path('login/', account.login, name='login'),
    path('register/', account.register, name='register'),

    # 首页
    path('home/', manage.home, name='home'),
    path('logout/', manage.logout, name='logout'),

    # 产品
    path('product_manage/', project.product_manage, name='product_manage'),
    path('product_add/', project.product_add, name='product_add'),
    path('product_delete/', project.product_delete, name='product_delete'),
    path('product_update/<int:pro_id>/', project.product_update, name='product_update'),
    path('product_search/', project.product_search, name='product_search'),

    # 单一接口用例
    path('apis_manage/', apis.apis_manage, name='apis_manage'),
    path('apis_add/', apis.apis_add, name='apis_add'),
    path('apis_delete/', apis.apis_delete, name='apis_delete'),
    path('apis_update/<int:apis_id>/', apis.apis_update, name='apis_update'),
    path('apis_search/', apis.apis_search, name='apis_search'),

    # 流程接口用例
    path('api_test_manage/', api_test.api_test_manage, name='api_test_manage'),
    path('api_test_add/', api_test.api_test_add, name='api_test_add'),
    path('api_test_delete/', api_test.api_test_delete, name='api_test_delete'),
    path('api_test_update/<int:api_t_id>/', api_test.api_test_update, name='api_test_update'),
    path('api_test_search/', api_test.api_test_search, name='api_test_search'),

    # 流程接口步骤用例
    path('api_step_manage/', api_test.api_step_manage, name='api_step_manage'),
    path('api_step_add/', api_test.api_step_add, name='api_step_add'),
    path('api_step_delete/', api_test.api_step_delete, name='api_step_delete'),
    path('api_step_update/', api_test.api_step_update, name='api_step_update'),
    path('api_test_search/', api_test.api_step_search, name='api_step_search'),

    # webUI用例
    path('web_test_manage/', web_test.web_test_manage, name='web_test_manage'),

    # appUI用例
    path('app_test_manage/', app_test.app_test_manage, name='app_test_manage'),

]
