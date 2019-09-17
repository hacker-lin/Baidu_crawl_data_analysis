import os
import random
import string
import requests
from django.http import HttpResponse, JsonResponse
from BaiduOnline.settings import CHART_DIR

from django.views import View

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializer import AnswerSerializer, FirstSerializer, SecondSerializer, ThirdSerializer, SmsSerializer, \
    UserRegSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .filter import AnswerFilter, FirstFilter, SecondFilter, ThirdFilter
from .models import AnswerQuestion, FirstCategory, SecondCategory, ThirdCategory, VerifyCode, UserProfile

from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer


# (1)
# class AnswerView(APIView):
#     def get(self, request):
#         answer_object = AnswerQuestion.objects.all()[0:10]
#         answer_serializer = AnswerSerializer(answer_object, many=True)
#         print(answer_serializer.data)
#         return Response(answer_serializer.data)
#
#     def post(self, request):
#         serializer = AnswerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# (2)
# class AnswerView(mixins.ListModelMixin, GenericAPIView):
#     """包含分页之类的组件  GenericAPIView"""
#     queryset = AnswerQuestion.objects.all()[:10]
#     serializer_class = AnswerSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# (3)
# class AnswerView(ListAPIView):
#     """封装上秒你的 GenericAPIView"""
#     queryset = AnswerQuestion.objects.all()
#     serializer_class = AnswerSerializer


#
# class AnswerView(ListAPIView):
#     pagination_class = AnswerPagination
#
#     queryset = AnswerQuestion.objects.all()
#     serializer_class = AnswerSerializer

# (5) 路由
# class AnswerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     pagination_class = AnswerPagination
#     queryset = AnswerQuestion.objects.all()
#     serializer_class = AnswerSerializer

# (6) 过滤器
# class AnswerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     pagination_class = AnswerPagination
#     serializer_class = AnswerSerializer
#     def get_queryset(self):
#         queryset = AnswerQuestion.objects.all()
#         # queryset = queryset.filter(xxx)
#         return queryset

# (4) 自定义分页
class AnswerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'p'
    max_page_size = 100


class FirstViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = FirstSerializer
    queryset = FirstCategory.objects.all()
    # filter_class = FirstFilter

    pagination_class = AnswerPagination  # 分页
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # 过滤（过滤，搜索，排序）

    search_fields = ('first_name',)
    ordering_fields = ('first_name',)


class SecondViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SecondSerializer
    queryset = SecondCategory.objects.all()
    # filter_class = SecondFilter

    pagination_class = AnswerPagination  # 分页
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # 过滤（过滤，搜索，排序）

    search_fields = ('second_name',)
    ordering_fields = ('second_name',)


class ThirdViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ThirdSerializer
    queryset = ThirdCategory.objects.all()
    # filter_class = ThirdFilter

    pagination_class = AnswerPagination  # 分页
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # 过滤（过滤，搜索，排序）

    search_fields = ('third_name',)
    ordering_fields = ('third_name',)


# (7) 过滤器升级
class AnswerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = AnswerSerializer
    queryset = AnswerQuestion.objects.all()
    # filter_class = AnswerFilter

    pagination_class = AnswerPagination  # 分页
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # 过滤（过滤，搜索，排序）

    search_fields = ('question', 'answer', 'third_id', 'question_time')
    ordering_fields = ('question', 'answer', 'third_id', 'question_time')


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        code = ''.join(random.choices(string.digits, k=4))
        sms_dict = requests.post(
            url='https://sms.yunpian.com/v2/sms/single_send.json',
            data={
                'apikey': '4bd1e2d7698475608acb0fc9679a4efb',
                'text': '312312321',
                'mobile': mobile
            },
        ).json()

        if sms_dict['code'] != 0:  # 返回0代表成功
            return Response({
                'mobile': sms_dict['msg']
            }, status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED)


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = UserProfile.objects.all()


class PlotView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'plot.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class BarView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'bar.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class CloudView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'cloud.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class MatrixView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'matrix.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class PieView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'pie.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class PyramidView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'Pyramid.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class SunView(View):
    def get(self, request):
        with open(os.path.join(CHART_DIR, 'sun.json'), encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='application/json')


class QuestionView(View):
    def post(self, request):
        question = request.data.get('question')
        print(question)


from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://39.107.86.223:6800')

class SpiderView(View):
    def get(self, request):
        state_dict = scrapyd.list_jobs('Baidu')
        if request.GET.get('tag') == 'start':
            scrapyd.schedule('Baidu', 'zhidao') # 'project_name', 'spider_name'
            return HttpResponse('0')
        if request.GET.get('tag') == 'stop':
            try:
                state = state_dict['running'][0]['id']
            except:
                return HttpResponse('-1')

            scrapyd.cancel('Baidu', state)  # 'project_nae' '状态值'
            return HttpResponse('0')
        return HttpResponse('')

