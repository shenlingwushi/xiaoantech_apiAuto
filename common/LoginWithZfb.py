# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 11:04
@File    : LoginWithZfb.py
@Description : 
@progname: xz_api_auto	
"""
import json

import requests

url = "http://preapi.smartbike.xiaoantech.com/java/led/application/v1/app/login/loginWithZfb"

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

getData = {
	"zfbAppId": ["2021003175692262"],
	"bikeIMEI": [""],
	"activityCode": [""],
	"authCode": ["c1a053d4246041e4881eae97f16fSC69"],
	"lng": ["114.43499050564236"],
	"cabinetSN": [""],
	"xcAppId": ["5d317d70d0d21c2a5adb5c0c"],
	"encryptedData": ["{\"response\":\"rD6VunsoN1nDz4q2qLusJ58FtrKFe6U3j2oqSH0awCVfv9PWVN79b79KOpMFydZLhD95/Lwlkozyecu0DRJk1g==\",\"sign\":\"ZML5ViDuwWpVy+kDDp+I0dgKtN+BPA+9lBnEBBoooAxS/4kVxbj/1wxJlddJwpuZ38qXhgHM1 QFMlPjKLeYibQW4JxACSZYPjA9ZB/pM/Y5dL2QweDBkpX54y2cWPi5eAlEgZrplkoB8CBa/BBiwz5qGHAz8SwG++rZs5hzxDlPWT2F1i4aOPWXj64yZ9jZWbwP8V4L2iraGTyWHEfZuL0/y3AEFWdW2vUGiisyZmvdkPIWhDqVT/ymGin8PDBJqfPjAwmZ/+GqTy8G4Z1+SKvG zZEgZxqHrCjZ5zEYpMXse27+Pu5wgj6z8o7EYuCXpBzcM/5s86JschstuTYdFQg==\"}"],
	"shopId": [""],
	"channelId": [""],
	"lat": ["30.50040554470486"],
	"recommendCode": [""]
}

response = requests.get(url, headers=headers,params=getData)
print(response.text)
print(json.loads(response.text)["data"]["signKey"])