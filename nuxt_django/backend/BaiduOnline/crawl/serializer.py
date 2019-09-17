from datetime import datetime, timedelta

import re
from rest_framework.validators import UniqueValidator

re_phone = re.compile(r"^1[35678]\d{9}$")

from rest_framework import serializers
from .models import AnswerQuestion, FirstCategory, SecondCategory, ThirdCategory, VerifyCode, UserProfile


# class AnswerSerializer(serializers.Serializer):
#     question = serializers.CharField(required=True, max_length=100)
#     answer = serializers.CharField(required=False, max_length=250)
#     third_id = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         # 接受前端传递过来的数据
#         return AnswerQuestion.objects.create(**validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = '__all__'


class ThirdSerializer(serializers.ModelSerializer):
    # third_answer = AnswerSerializer(many=True)

    class Meta:
        model = ThirdCategory
        fields = '__all__'


class SecondSerializer(serializers.ModelSerializer):
    # second_third = ThirdSerializer(many=True)

    class Meta:
        model = SecondCategory
        fields = '__all__'


class FirstSerializer(serializers.ModelSerializer):
    # first_second = SecondSerializer(many=True)

    class Meta:
        model = FirstCategory
        fields = '__all__'


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, label='手机号')

    def validate_mobile(self, mobile):
        """钩子函数"""
        if UserProfile.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        # 验证手机号
        if not re_phone.match(mobile):
            raise serializers.ValidationError('手机号格式非法！')

        # 获取一分钟之前的时间
        one_minute = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)

        # 如果是在这个一分钟之内
        if VerifyCode.objects.filter(add_time__gt=one_minute, mobile=mobile).count():
            raise serializers.ValidationError('1分钟之内，发送太频繁，请稍后再试')

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, min_length=4, help_text='验证码', label='验证码',
                                 write_only=True)
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all(), message="用户已经存在")])
    mobile = serializers.CharField(label="手机号")

    password = serializers.CharField(style={'input_type': 'password'}, label='密码', write_only=True)



    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validata_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by('-add_time')
        if verify_records:
            last_records = verify_records[0]

            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=5)
            if five_minute_ago > last_records.add_time:
                raise serializers.ValidationError('验证码过期！')
            if last_records.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误！')

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = UserProfile
        fields = ('username', 'code', 'mobile', 'password')
