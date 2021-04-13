# -*- coding:utf-8 -*-

# @Time : 2021/4/12 0:00 
# @Author : rain
# @File : logger.py

import logging
from question_bank.settings import LOGGER_NAME, LOGGER_LEVEL


logger = logging.getLogger(LOGGER_NAME)
logging.basicConfig(level=LOGGER_LEVEL)