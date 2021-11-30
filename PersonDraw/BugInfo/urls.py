# -*- coding: utf-8 -*-
# @Time     : 2021/11/8 16:22
# @Author   : fanzhaoran
# @File     : urls.py
from django.urls import path
from . import views

urlpatterns = [
    # TODO person_info 路由设置
    path('bugInfo/', views.bugInfo, name="bugInfo"),
]
