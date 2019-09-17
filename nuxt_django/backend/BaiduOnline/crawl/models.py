from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='', null=True, blank=True)
    birday = models.DateField(verbose_name='生日', blank=True, null=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=10, null=True,
                              blank=True)
    address = models.CharField(max_length=100, default='', null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100, null=True,
                              blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        db_table = 'UserProfile'

    def __str__(self):
        return self.username


class FirstCategory(models.Model):
    first_id = models.CharField(primary_key=True, max_length=3, verbose_name='领域编号', help_text='领域编号')
    first_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='领域名称', help_text='领域名称')

    class Meta:
        managed = False
        db_table = 'first_category'
        verbose_name = '领域'
        verbose_name_plural = verbose_name
        ordering = ['first_id']

#    def __str__(self):
#        return self.first_name


class SecondCategory(models.Model):
    second_id = models.CharField(primary_key=True, max_length=6, verbose_name='行业编号', help_text='行业编号')
    second_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='行业名称', help_text='行业名称')
    first_id = models.ForeignKey(FirstCategory, on_delete=models.CASCADE, related_name='first_second', blank=True,
                                 null=True, verbose_name='领域编号',
                                 help_text='领域编号')

    class Meta:
        managed = False
        db_table = 'second_category'
        verbose_name = '行业'
        verbose_name_plural = verbose_name
        ordering = ['second_id']

    def __str__(self):
        return self.second_name


class ThirdCategory(models.Model):
    third_id = models.CharField(primary_key=True, max_length=16, verbose_name='分类编号', help_text='分类编号')
    third_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='分类名称', help_text='分类名称')
    # second_id = models.CharField(max_length=6, verbose_name='行业编号', help_text='行业编号')
    second_id = models.ForeignKey(SecondCategory, on_delete=models.CASCADE, related_name='second_third', blank=True,
                                  null=True, verbose_name='行业编号',
                                  help_text='行业编号')

    class Meta:
        managed = False
        db_table = 'third_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['third_id']

    def __str__(self):
        return self.third_name


class AnswerQuestion(models.Model):
    question = models.CharField(max_length=100, blank=True, null=True, verbose_name='问题', help_text='问题')
    answer = models.CharField(max_length=250, blank=True, null=True, verbose_name='回答', help_text='回答')
    # third_id = models.CharField(max_length=16, verbose_name='分类编号', help_text='分类编号')
    question_time = models.CharField(max_length=25, blank=True, null=True, verbose_name='提问时间', help_text='提问时间')
    third_id = models.ForeignKey(ThirdCategory, on_delete=models.CASCADE, related_name='third_answer', blank=True,
                                 null=True, verbose_name='分类编号',
                                 help_text='分类编号')

    class Meta:
        managed = False
        db_table = 'answer_question'
        verbose_name = '问答'
        verbose_name_plural = verbose_name

#    def __str__(self):
#        return self.question


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'VerifyCode'
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
