# -*- coding:utf-8 -*-

# @Time : 2021/4/13 23:38 
# @Author : rain
# @File : pagination.py


from rest_framework.pagination import PageNumberPagination


class PageNumber(PageNumberPagination):

    def __init__(self, size=10):
        self.page_size = size
        self.max_page_size = size*10
        self.page_query_param = "offset"
        self.page_size_query_param = "limit"
