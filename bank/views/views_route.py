# -*- coding:utf-8 -*-

# @Time : 2021/4/11 23:55 
# @Author : rain
# @File : views_route.py

from __future__ import annotations
from .question import QuestionInfo


get_question_info = QuestionInfo.as_view({'post': 'get_question_info'})
add_question_info = QuestionInfo.as_view({'post': 'add_question_info'})
update_question_info = QuestionInfo.as_view({'post': 'update_question_info'})
