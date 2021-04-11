# -*- coding:utf-8 -*-

# @Time : 2021/4/10 22:15 
# @Author : rain
# @File : question_serializer.py

from __future__ import annotations
from rest_framework.serializers import ModelSerializer


from .question_model import Questions, DetailInfo, QuestionDetailRel


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Questions
        fields = ['question_id', 'title', 'type', 'status', 'version']


class DetailSerializer(ModelSerializer):

    class Meta:
        model = DetailInfo
        fields = ['detail_id', 'content', 'code', 'style', 'status', 'notes']


class QuestionDetailRelSerializer(ModelSerializer):

    class Meta:
        model = QuestionDetailRel
        fields = ['id', 'question_id', 'detail_id', 'status']
