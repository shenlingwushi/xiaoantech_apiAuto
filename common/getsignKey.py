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
import configparser
import requests

from utils.config_reader import read_config
from utils.excel_reader import read_appLoginMsg,read_sysLoginMsg

# 读取 Excel 文件中的测试用例
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_CASES_FILE = os.path.join(base_dir, "test_data\\testlogin.xlsx")
appLogin_message = read_appLoginMsg(TEST_CASES_FILE, "application")
sysLogin_message = read_sysLoginMsg(TEST_CASES_FILE, "system")

class GetAppSignKey:
    def getAppToken(self, login_message_app):
        url = f'{read_config("general_url")}' + login_message_app[0]
        method = login_message_app[1]
        params = json.loads(login_message_app[2])
        headers = {
                    "traceid": "17392441176163086155",
                    "referer": "https://2021003175692262.hybrid.alipay-eco.com/2021003175692262/0.3.2501061008.52/index.html#pages/login/login?__appxPageId=1",
                    "X-Request-ID": "9cbcd64210da4d0cebde32d91352ca66",
                    "X-Original-Forwarded-For": "223.104.119.88",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 14; PHM110 Build/ UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.148 MYWeb/0.11.0.241217113053 UWS/3.22.2.9999 UCBS/3.22.2.9999_220000000000 Mobile Safari/537.36 NebulaSDK/1.8.10011 2 Nebula AlipayDefined(nt:5G,ws:360|0|3.0) AliApp(AP /10.6.80.8000) AlipayClient/10.6.80.8000 Language/zh-Hans isConcaveScreen/false Region/CNAriver/1.0.0 ChannelId(5) DTN/2.0",
                    "Accept-Encoding": "gzip",
                    "authorization": "Bearer",
                    "content-type": "application/json ",
                    "X-Real-IP": "58.19.38.57",
                    "alipayMiniMark": "iOuGKtwstByqMosbL1Ksu7ZnpwJhg+uUtbsVuHqkwwY3+hhABTq7lo/tmtwzcyMowMW2Q7En6hi0vAizbUpq5gvmjJwckCFblShXb/j0YZU=",
                    "Cookie": "",
                    "Accept-Charset": "utf-8",
                    "X-Forwarded-Host": "preapi.smartbike.xiaoantech.com",
                    "X-Forwarded-Proto": "http",
                    "Host": "preapi.smartbike.xiaoantech.com",
                    "x-release-type": "DEBUG",
                    "X-Forwarded-Port": "80",
                    "accept": "application/json",
                    "appid": "2021003175692262",
                    "xFlag": "eGlhb2dlY2xpZW50OjEyMzQ1Ng==",
                    "citypinyin": "wuhanshi",
                    "X-Forwarded-For": "58.19.38.57",
                    "X-Forwarded-Scheme": "http",
                    "appfrom": "zfb",
                    "X-Scheme": "http"
                    }
        response = requests.request(method=method, url=url, params=params, headers=headers)
        signKey = response.json().get("data").get("signKey")
        return signKey

    def save_appToken_to_config(self,token):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        config['appBearToken'] = {'authorization': f'Bearer {token}'}
        with open('../config.ini', 'w') as configfile:
            config.write(configfile)

    def load_appToken_from_config(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        return config["appBearToken"].get("authorization")

# 从system登录接口中获取和保存secret值
class GetSysSignKey:
    def getSysToken(self, login_message_sys):
        url = f'{read_config("general_url")}' + login_message_sys[0]
        method = login_message_sys[1]
        params = json.loads(login_message_sys[2])
        headers = {
                    "User-Agent":"Mozilla/5.0 (Linu x; Android 14; PHM110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300289 MMWEBSDK/20241103 MMWEBID/490 MicroMessenger/8.0.5 4.2760(0x28003653) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
                    "traceId":"1372013819213720138192",
                    "charset":"utf-8",
                    "X-Request-ID":"560a772c6f00fc28ef96b5465feeed8a",
                    "X-Forwarded-Host":"preapi.smartbike.xiaoantech.com",
                    "X-Forwarded-Proto":"http",
                    "Host":"preapi.smartbike.xiaoantech.com",
                    "Accept-Encoding":"gzip, deflate",
                    "rwarded-Port":"80",
                    "accept":"application/json",
                    "innertenantid":"D2W2438*TI00st9#C./*HQ[pk;lm8neFE2WcNFd",
                    "xFlag":"eGlhb2dlb3BlcmF0aW9uOjEyMzQ1Ng==",
                    "X-Forwarded-For":"223.104.122.",
                    "content-type":"application/json",
                    "Content-Length":"129",
                    "X-Real-IP":"223.104.122.10",
                    "X-Forwarded-Scheme":"http",
                    "X-Scheme":"http"
                    }
        response = requests.request(method=method, url=url, json=params, headers=headers)
        secret = response.json().get("data").get("secret")
        return secret

    def save_sysToken_to_config(self,token):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        config['sysBearToken'] = {'authorization': f'Bearer {token}'}
        with open('../config.ini', 'w') as configfile:
            config.write(configfile)

    def load_sysToken_from_config(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        return config["sysBearToken"].get("authorization")

# getSystemSignKey = GetSysSignKey()
# print(getSystemSignKey.getSysToken(sysLogin_message))
#
# getSystemSignKey.save_sysToken_to_config(getSystemSignKey.getSysToken(sysLogin_message))
# secret = getSystemSignKey.load_sysToken_from_config()
# print("secret",secret)