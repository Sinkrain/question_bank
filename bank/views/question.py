# -*- coding: utf-8 -*-

from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework import status
from django.http import JsonResponse

from utils import pre_params_check, logger, ResponseBody
from bank.models import Questions, QuestionDetailRel, QuestionSerializer


class QuestionInfo(ViewSet):

    get_params = ("offset", "limit")
    add_params = ("title", "style")
    update_params = ("id", "version")

    @pre_params_check(get_params)
    def get_question_info(self, request: Request, data: dict):
        offset = data.get("offset")
        limit = data.get("limit")
        logger.info("Params: offset={} limit={}".format(offset, limit))
        question = Questions.objects.all()
        serializer_class = QuestionSerializer(question, many=True)
        data = ResponseBody().content
        data['data'] = serializer_class.data
        return JsonResponse(data, status=status.HTTP_200_OK)

    @pre_params_check(add_params)
    def add_question_info(self, request: Request, data: dict):
        pass

    @pre_params_check(update_params)
    def update_question_info(self, request: Request, data: dict):
        pass