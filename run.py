# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/12 14:23
@File    : run.py
@Description : 
@progname: xz_api_auto	
"""
import os
import pytest

if __name__ == "__main__":
	pytest.main(['test_cases/test_all_case.py', '-vs', '-q', '--alluredir', './allure-results'])
	os.system('allure generate ./allure-results -o ./report --clean')

	report_path = os.path.join(os.path.dirname(__file__), 'report')
	bat_file_path = os.path.join(os.path.dirname(__file__), 'click.bat')
	if os.listdir(report_path):
		with open(bat_file_path, 'w') as f:
			f.write("allure open report")
