# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 22:02
@File    : conftest.py
@Description : 
@progname: xz_api_auto	
"""
from datetime import datetime

import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_session():
	from utils.logger import logger
	logger.info(f"=== 测试开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
	yield
	logger.info(f"=== 测试结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
