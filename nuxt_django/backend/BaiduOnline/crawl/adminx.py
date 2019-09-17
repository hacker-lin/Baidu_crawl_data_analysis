import xadmin
# from django.contrib.auth.models import User
from xadmin.plugins.auth import ChangePasswordView

from .models import FirstCategory, SecondCategory, ThirdCategory, AnswerQuestion, VerifyCode, UserProfile
from xadmin import views

from django.contrib.auth import get_user_model

User = get_user_model()

xadmin.site.register_view(r'^users/userprofile/(.+)/password/$',
                          ChangePasswordView, name='user_change_password')


# class UserProfileAdmin:
#     list_display = ['username', 'mobile', 'email']
#     search_fields = ['username', 'mobile', 'email']
#     list_filter = ['username', 'mobile', 'email']
# xadmin.site.register(UserProfile, UserProfileAdmin)

class FirstCategoryAdmin(object):
    list_display = ['first_id', 'first_name']
    search_fields = ['first_id', 'first_name']
    list_filter = ['first_id', 'first_name']


class SecondCategoryAdmin(object):
    list_display = ['second_id', 'second_name', 'first_id']
    search_fields = ['second_id', 'second_name', 'first_id']
    list_filter = ['second_id', 'second_name', 'first_id']


class ThirdCategoryAdmin(object):
    list_display = ['third_id', 'third_name', 'second_id']
    search_fields = ['third_id', 'third_name', 'second_id']
    list_filter = ['third_id', 'third_name', 'second_id']


class AnswerQuestionAdmin(object):
    list_display = ['question', 'answer', 'question_time', 'third_id']
    search_fields = ['question', 'answer', 'question_time', 'third_id']
    list_filter = ['question', 'answer', 'question_time', 'third_id']


# class VerifyCodeAdmin(object):
#     list_display = ['code', 'mobile', 'add_time']
#     search_fields = ['code', 'mobile', 'add_time']
#     list_filter = ['code', 'mobile', 'add_time']


xadmin.site.register(FirstCategory, FirstCategoryAdmin)
xadmin.site.register(SecondCategory, SecondCategoryAdmin)
xadmin.site.register(ThirdCategory, ThirdCategoryAdmin)
xadmin.site.register(AnswerQuestion, AnswerQuestionAdmin)
# xadmin.site.register(VerifyCode, VerifyCodeAdmin)



class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSettings)


class GlobalSettings(object):
    site_title = 'Cython_lin'
    site_footer = 'Cython_lin'
    menu_style = 'accordion'  # 列表折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)
