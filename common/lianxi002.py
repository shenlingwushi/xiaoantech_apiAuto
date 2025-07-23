# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/26 16:19
@File    : lianxi002.py
@Description : 
@progname: xz_api_auto	
"""

import requests

# url1 = 'http://preapi.smartbike.xiaoantech.com/java/led/system/v1/platform/permission/user/login'
# method1 = 'POST'
# params1 = {
#  "username": "18600000000",
#  "password": "4E792A533989F212D1BAB0CE54C1DE8E6B67AABA"
# }
# headers1 = {
# 	"User-Agent": "Mozilla/5.0 (Linu x; Android 14; PHM110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300289 MMWEBSDK/20241103 MMWEBID/490 MicroMessenger/8.0.5 4.2760(0x28003653) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
# 	"traceId": "1372013819213720138192",
# 	"charset": "utf-8",
# 	"X-Request-ID": "560a772c6f00fc28ef96b5465feeed8a",
# 	"X-Forwarded-Host": "preapi.smartbike.xiaoantech.com",
# 	"X-Forwarded-Proto": "http",
# 	"Host": "preapi.smartbike.xiaoantech.com",
# 	"Accept-Encoding": "gzip, deflate",
# 	"rwarded-Port": "80",
# 	"accept": "application/json",
# 	"innertenantid": "D2W2438*TI00st9#C./*HQ[pk;lm8neFE2WcNFd",
# 	"xFlag": "eGlhb2dlb3BlcmF0aW9uOjEyMzQ1Ng==",
# 	"X-Forwarded-For": "223.104.122.",
# 	"content-type": "application/json",
# 	"Content-Length": "129",
# 	"X-Real-IP": "223.104.122.10",
# 	"X-Forwarded-Scheme": "http",
# 	"X-Scheme": "http"
# }
# response = requests.request(method=method1, url=url1, json=params1, headers=headers1)
# secret = response.json().get("data").get("secret")
#
#
# url2 = f'http://preapi.smartbike.xiaoantech.com/java/led/system/v1/platform/shop/queryShop'
# method2 = 'GET'
# params2 = {"name":"佳园路","isEnable":"true"}
# header2 = {
# 		"Accept":"application/json, text/plain, */*",
# 		"Accept-Encoding":"gzip, deflate",
# 		"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
# 		"Connection":"keep-alive",
# 		"Content-Type":"application/json;charset=UTF-8",
# 		"User-Agent":"Mozilla/5.0 (Linu x; Android 14; PHM110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300289 MMWEBSDK/20241103 MMWEBID/490 MicroMessenger/8.0.5 4.2760(0x28003653) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
# 		"Authorization":f"{secret}"
# 		}
# response = requests.request(method2, url2, headers=header2, params=params2)
#
# print(response.json())

abc = 'wangcongyu'

print(abc[:4])