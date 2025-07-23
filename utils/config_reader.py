# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/13 14:59
@File    : config_reader.py
@Description : 
@progname: xz_api_auto	
"""

import configparser
import json
import os

config_path = os.path.join(os.path.dirname(__file__), '..','config.ini')
def read_config(params) -> object:
	config = configparser.ConfigParser()
	config.read(config_path)
	if params == 'general_url':
		return config.get("base_http_url","general_url")

	elif params == 'app_header':
		return json.loads(config.get("otherparams","general_app_header"))

	elif params == 'sys_header':
		return json.loads(config.get("otherparams","general_sys_header"))

	else:
		print("传入读取配置文件的参数有误")

# print(read_config("sys_header"))
# print(type(read_config("sys_header")))
# print(read_config("general_url"))
# print(type(read_config("general_url")))