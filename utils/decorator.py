# -*- coding:utf-8 -*-

# @Time : 2021/4/12 0:12 
# @Author : rain
# @File : decorator.py

from __future__ import annotations
import json
import functools
import traceback
from rest_framework import status
from django.http import HttpRequest, JsonResponse
from utils.logger import logger
from utils.exception import ParamsCheckError, CustomizeError
from utils.response_style import ResponseBody


def pre_params_check(params: (list, tuple, str)):

    def _decorator(func):

        @functools.wraps(func)
        def _wraps(self, request: HttpRequest, *args, **kwargs):
            body = ResponseBody().content
            try:
                logger.info(" {} {} ".format(request.method, request.get_full_path()).center(52, "#"))
                logger.debug("Request Headers: {}".format(request.headers))
                if request.method == "GET" and request.body == b"":
                    data = request.GET
                else:
                    data = json.loads(request.body)
                    logger.debug("Request Body: {}".format(data))
                    data = data["Params"]
                logger.info("Request Params: {}".format(data))
                pre_params = (params, ) if isinstance(params, str) else params
                for param in pre_params:
                    if data.get(param) is None:
                        body["code"] = 400
                        body["message"] = "'{}' ParamsError, Please Check !".format(param)
                        raise ParamsCheckError(JsonResponse(data=body, status=status.HTTP_400_BAD_REQUEST))

                return func(self, request, data)
            except (ParamsCheckError, CustomizeError) as e:
                return e.response
            except Exception:
                body["code"] = 500
                body["message"] = "server Error !"
                logger.error(traceback.format_exc())
                return JsonResponse(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return _wraps
    return _decorator
