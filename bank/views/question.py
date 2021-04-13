# -*- coding: utf-8 -*-

from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework import status
from django.http import JsonResponse

from utils import pre_params_check, logger, ResponseBody
from bank.models import Questions, QuestionDetailRel, QuestionSerializer
from bank.views.pagination import PageNumber


class QuestionInfo(ViewSet):

    get_params = ("offset", "limit")
    add_params = ("title", "type")
    update_params = ("id", "version")

    @pre_params_check(get_params)
    def get_question_info(self, request: Request, data: dict):
        offset = data.get("offset")
        limit = int(data.get("limit"))
        logger.info("Params: offset={} limit={}".format(offset, limit))
        question = Questions.objects.all()
        pagination = PageNumber(limit)
        count = len(question)
        pagination_data = pagination.paginate_queryset(question, request)
        logger.debug("pagination_data: {}".format(pagination_data))

        serializer_class = QuestionSerializer(pagination_data, many=True)
        data = ResponseBody().content
        data['data'] = {
            "questions": serializer_class.data,
            "count": count
        }
        return JsonResponse(data, status=status.HTTP_200_OK)

    @pre_params_check(add_params)
    def add_question_info(self, request: Request, data: dict):
        try:
            params = {
                "title": data.get('title'),
                "type": data.get('type'),
                "status": 10,
                "version": 1
            }
            serializer = QuestionSerializer(data=params)
            response = ResponseBody().content
            if serializer.is_valid():
                serializer.save()
                response["data"] = serializer.data
                response["message"] = "Successful add question"
                return JsonResponse(response, status=status.HTTP_200_OK)
            response["data"] = serializer.errors
            response["message"] = "Error, when add, please check"
            response["code"] = 400
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            raise

    @pre_params_check(update_params)
    def update_question_info(self, request: Request, data: dict):
        pass