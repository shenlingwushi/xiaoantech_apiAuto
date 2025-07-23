# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 17:14
@File    : config_operate_api.py
@Description : 
@progname: xz_api_auto	
"""

import os


class Config:
	@staticmethod
	def getconf(filepath):
		return os.path.dirname(filepath)
