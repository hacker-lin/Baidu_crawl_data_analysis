import django_filters as df
from django_filters.rest_framework import FilterSet

from crawl.models import AnswerQuestion, FirstCategory, SecondCategory, ThirdCategory


class FirstFilter(FilterSet):
    first_name = df.CharFilter('first_name', lookup_expr='contains', label='请输入一类包含的字段')

    class Meta:
        model = FirstCategory
        fields = ['first_name']


class SecondFilter(FilterSet):
    second_name = df.CharFilter('second_name', lookup_expr='contains', label='请输入二类包含的字段')

    class Meta:
        model = SecondCategory
        fields = ['second_name']


class ThirdFilter(FilterSet):
    third_name = df.CharFilter('third_name', lookup_expr='contains', label='请输入三类包含的字段')

    class Meta:
        model = ThirdCategory
        fields = ['third_name']


class AnswerFilter(FilterSet):
    question_like = df.CharFilter('question', lookup_expr='contains', label='请输入问题包含的字段')
    answer_like = df.CharFilter('answer', lookup_expr='contains', label='请输入答案包含的字段')

    class Meta:
        model = AnswerQuestion
        fields = ['question_like', 'answer_like']
