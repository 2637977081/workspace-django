"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from HelloWorld import view, wx

urlpatterns = [
    # Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name。
    #
    # 语法格式：
    # path(route, view, kwargs=None, name=None)
    # route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
    # view: 用于执行与正则表达式匹配的 URL 请求。
    # kwargs: 视图使用的字典类型的参数。
    # name: 用来反向获取 URL。
    #
    path('', view.login_page),
    path('hello', view.helloHtml),
    path('login/page', view.login_page),
    path('login',view.login),
    path('change',view.chang),
    path('send/email',view.send_email),
    path('wx',wx.wx_verification),
    path('cat',view.cat),
]
