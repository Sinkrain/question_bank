# -*- coding:utf-8 -*-

# @Time : 2021/4/12 0:09 
# @Author : rain
# @File : exception.py

from django.http import HttpResponse


class BaseExceptionError(Exception):

    def __init__(self, response: HttpResponse, message='', code=0):
        self.response = response
        self.message = message
        self.code = code


class CustomizeError(BaseExceptionError):

    pass


class ParamsCheckError(BaseExceptionError):

    pass