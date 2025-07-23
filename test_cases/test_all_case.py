# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 21:46
@File    : getsignKey.py
@Description : 
@progname: xz_api_auto	
"""
import json
import os
from urllib.parse import quote

import allure
import configparser
import pytest
import requests

from utils.config_reader import read_config, config_path
from utils.logger import logger
from utils.excel_reader import read_appLoginMsg, read_sysLoginMsg, read_app_test_cases, read_sys_test_cases
from common.getsignKey import GetAppSignKey, GetSysSignKey
from utils.download_file import download_excel

# 读取 Excel 文件中的测试用例
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_CASES_FILE = os.path.join(base_dir, "test_data\\testlogin.xlsx")
appLogin_message = read_appLoginMsg(TEST_CASES_FILE, "application")
sysLogin_message = read_sysLoginMsg(TEST_CASES_FILE, "system")
test_app_cases = read_app_test_cases(TEST_CASES_FILE, "application")
test_sys_cases = read_sys_test_cases(TEST_CASES_FILE, "system")

@allure.feature("接口测试")
class TestCaseExe:
    @pytest.fixture()
    def my_fixture_app(self):
        print("初始化资源!!!!!!")

        getApplicationSignKey = GetAppSignKey()
        getApplicationSignKey.save_appToken_to_config(getApplicationSignKey.getAppToken(appLogin_message))
        token = getApplicationSignKey.load_appToken_from_config()
        # 将登录的signKey值传给application的测试用例
        yield token

        print("清理资源!!!!!! ")

    @pytest.fixture()
    def my_fixture_sys(self):
        print("初始化资源!!!!!!")

        getSystemSignKey = GetSysSignKey()
        getSystemSignKey.save_sysToken_to_config(getSystemSignKey.getSysToken(sysLogin_message))
        secret = getSystemSignKey.load_sysToken_from_config()
        # 将登录的secret值传给system的测试用例
        yield secret
        print("清理资源!!!!!! ")

    @allure.story("saasApplication接口测试")
    # @allure.title("{case_name}")
    @pytest.mark.parametrize("case", test_app_cases,ids=[case["case_name"] for case in test_app_cases])
    def test_application(self, case, my_fixture_app):
        allure.dynamic.title(case["case_name"])
        with allure.step("准备请求数据"):
            method = case["method"]
            url = f'{read_config("general_url")}' + case["url"]
            app_headers = read_config("app_header")
            app_headers["authorization"] = my_fixture_app
            headers = app_headers
            params = case["params"]
            logger.info(f"请求方法: {method}")
            logger.info(f"请求URL: {url}")
            logger.info(f"请求头: {headers}")
            logger.info(f"请求参数: {params}")

        with allure.step("发送请求"):
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=params)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=params)
            else:
                raise ValueError(f"不支持的请求方法: {method}")

            logger.info(f"响应状态码: {response.status_code}")
            logger.info(f"响应内容: {response.json()}")

        # if response.json

        with allure.step("验证响应状态码"):
            assert response.status_code == case["expected_status"], \
                f"预期状态码: {case['expected_status']}, 实际状态码: {response.status_code}"

        with allure.step("验证响应内容"):
            if case["assert_key"] and case["assert_value"]:
                response_data = response.json()
                assert case["assert_key"] in response_data, f"响应中未找到字段: {case['assert_key']}"
                assert response_data[case["assert_key"]] == case["assert_value"], \
                    f"预期值: {case['assert_value']}, 实际值: {response_data[case['assert_key']]}"


    @allure.story("saasSystem接口测试")
    # @allure.title("{case_name}")
    @pytest.mark.parametrize("case", test_sys_cases,ids=[case["case_name"] for case in test_sys_cases])
    def test_system(self, case, my_fixture_sys):
        allure.dynamic.title(case["case_name"])
        with allure.step("准备请求数据"):
            method = case["method"]
            url = f'{read_config("general_url")}' + case["url"]
            sys_headers = read_config("sys_header")
            sys_headers["Authorization"] = my_fixture_sys
            headers = sys_headers
            params = case["params"]
            logger.info(f"请求方法: {method}")
            logger.info(f"请求URL: {url}")
            logger.info(f"请求头: {headers}")
            logger.info(f"请求参数: {params}")

        if '/java/led/system/v1/platform/user/list' in case["url"] and {"pageSize":"50","pageNum":"1"} == case['params']:
            with allure.step("发送请求"):
                response = requests.get(url, headers=headers, params=params)
                # 获取第一个骑手的userId并写入配置文件
                userId = response.json()['data']['list'][0]["id"]
                if userId:
                    config = configparser.ConfigParser()
                    config.read(config_path)
                    config['otherparams']["userid"] = f'{userId}'
                    logger.info("获取到骑手userId:" + f'{userId}')
                    with open(config_path, 'w') as configfile:
                        config.write(configfile)
                else:
                    logger.info("未获取到骑手userId!")

        elif '/java/led/system/v1/platform/cabinet/list' in case["url"]:
            with allure.step("发送请求"):
                response = requests.get(url, headers=headers, params=params)
                # 获取第一个电柜的SN并写入配置文件
                cabinetsn = response.json()['data']['list'][0]["cabinetSN"]
                if cabinetsn:
                    config = configparser.ConfigParser()
                    config.read(config_path)
                    config['otherparams']["cabinetsn"] = f'{cabinetsn}'
                    logger.info("获取到电柜SN:" + f'{cabinetsn}')
                    with open(config_path, 'w') as configfile:
                        config.write(configfile)
                else:
                    logger.info("未获取到电柜SN!")

        elif '/java/led/system/v1/platform/excel/exportList' in case['url'] and (0 < int(case['params']['fileType']) < 101 ):
            with allure.step("发送请求"):
                response = requests.get(url, headers=headers, params=params)
                # 获取用户报表的第1个文件信息
                subDir = response.json()['data']['list'][0]["subDir"]
                file_name = response.json()['data']['list'][0]["name"]
                encoded = quote(file_name[:4],encoding = 'utf-8')
                file_path = 'https://xc-led.oss-cn-hangzhou.aliyuncs.com/exportFiles/' + subDir + '/' + encoded + file_name[-20:]
                download_excel(file_path,file_name)
                print("这里是从用例处进行调用")
                logger.info(f"响应状态码: {response.status_code}")
                logger.info(f"响应内容: {response.json()}")

        else:
            with allure.step("发送请求"):
                if method.upper() == "GET":
                    response = requests.get(url, headers=headers, params=params)
                elif method.upper() == "POST":
                    response = requests.post(url, headers=headers, json=params)
                elif method.upper() == "PUT":
                    response = requests.put(url, headers=headers, json=params)
                elif method.upper() == "DELETE":
                    response = requests.delete(url, headers=headers, params=params)
                else:
                    raise ValueError(f"不支持的请求方法: {method}")

                logger.info(f"响应状态码: {response.status_code}")
                logger.info(f"响应内容: {response.json()}")

        with allure.step("验证响应状态码"):
            assert response.status_code == case["expected_status"], \
                f"预期状态码: {case['expected_status']}, 实际状态码: {response.status_code}"

        with allure.step("验证响应内容"):
            if case["assert_key"] and case["assert_value"]:
                response_data = response.json()
                assert case["assert_key"] in response_data, f"响应中未找到字段: {case['assert_key']}"
                assert response_data[case["assert_key"]] == case["assert_value"], \
                    f"预期值: {case['assert_value']}, 实际值: {response_data[case['assert_key']]}"