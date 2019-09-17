"""BaiduOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
import xadmin
from rest_framework_jwt.views import obtain_jwt_token

from crawl.views import AnswerViewSet, FirstViewSet, SecondViewSet, ThirdViewSet, SmsCodeViewSet, UserViewSet, PlotView, \
    QuestionView, SpiderView
from rest_framework.authtoken import views

from django.views import static
from django.conf import settings
from django.conf.urls import url


# (1) as_view
# answer_list = AnswerView.as_view({
#     'get': 'list',
#     # 'post': 'create'
# })


# (2) router代替 as_view
router = DefaultRouter()

router.register('first', FirstViewSet, base_name='first')
router.register('second', SecondViewSet, base_name='second')
router.register('third', ThirdViewSet, base_name='third')
router.register('answer', AnswerViewSet, base_name='answer')  # 自动将 get-转到list上，并且收集所有url，下面注册直接include(router.urls)即可

urlpatterns = [
    re_path('^xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Response界面的登录按钮
    re_path(r'^docs/', include_docs_urls(title='百度知道')),
    re_path(r'^', include(router.urls)),
    re_path(r'^api-token-auth/', views.obtain_auth_token),  # django自带的 auth
    # re_path(r'^jwt_auth/', obtain_jwt_token),  # jwt插件
    re_path(r'^charts', include('crawl.urls')),
    # path('^question/<question>', QuestionView.as_view()),
    re_path(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path('^spider', SpiderView.as_view()),
]
