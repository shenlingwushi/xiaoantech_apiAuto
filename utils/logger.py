# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 21:44
@File    : logger.py
@Description : 
@progname: xz_api_auto	
"""

import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger."""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# 设置日志文件路径
log_file = os.path.join(os.getcwd(), 'test.log')
logger = setup_logger('test_logger', log_file)