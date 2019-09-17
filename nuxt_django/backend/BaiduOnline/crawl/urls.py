from django.urls import re_path
from .views import PlotView, BarView, CloudView, MatrixView, PyramidView, SunView, PieView

urlpatterns = [
    re_path(r'plot$', PlotView.as_view()),
    re_path(r'bar$', BarView.as_view()),
    re_path(r'cloud$', CloudView.as_view()),
    re_path(r'matrix$', MatrixView.as_view()),
    re_path(r'pyramid$', PyramidView.as_view()),
    re_path(r'sun$', SunView.as_view()),
    re_path(r'pie$', PieView.as_view()),

]
