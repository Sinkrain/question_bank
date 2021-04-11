# -*- coding:utf-8 -*-

# @Time : 2021/4/12 0:12 
# @Author : rain
# @File : decorator.py

from __future__ import annotations
import json
import functools
from django.http import HttpRequest, JsonResponse
from utils.logger import logger


def pre_params_check(params: (list, tuple, str)):

    def _decorator(func):

        @functools.wraps(func)
        def _wraps(self, request: HttpRequest, *args, **kwargs):
            logger.info(" {} {} ".format(request.method, request.get_full_path()).center(52, "#"))
            logger.debug("Request Headers: {}".format(request.headers))
            data = json.loads(request.body)
            logger.info("Request Body: {}".format(data))
            return func(self, request, data)
        return _wraps
    return _decorator
