# from django.contrib import admin
from django.urls import path, include
# 导入drf提供的路由
from rest_framework.routers import DefaultRouter
from top.views import TmgAllOrderAPIview

# 将路由实例化
routers = DefaultRouter()

# 注册url
# (第一个参数)是地址： http://127.0.0.1:8000/api/v1/alipayorders 就可以马上访问
# (第二个参数)是视图： 进入该地址后，显示的视图类型
routers.register('top', TmgAllOrderAPIview, basename='查询卖家已卖出的交易数据（根据创建时间）')

urlpatterns = []

#自动添加路由
urlpatterns += routers.urls