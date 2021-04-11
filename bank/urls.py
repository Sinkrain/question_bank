# -*- coding:utf-8 -*-

# @Time : 2021/4/11 23:49 
# @Author : rain
# @File : urls.py

from django.conf.urls import url
from .views.views_route import get_question_info, add_question_info, update_question_info


urlpatterns = [
    url(r'question/getQuestionInfo/?$', get_question_info),
    url(r'question/addQuestionInfo/?$', add_question_info),
    url(r'question/updateQuestionInfo/?$', update_question_info)
]