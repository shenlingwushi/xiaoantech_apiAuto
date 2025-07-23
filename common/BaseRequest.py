# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 10:25
@File    : BaseRequest.py
@Description : 
@progname: xz_api_auto	
"""

import requests
from requests.exceptions import RequestException

class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Request failed: {e}")
            return None

class GetRequest(BaseRequest):
    def get(self, endpoint, params=None):
        return super().send_request('GET', endpoint, params=params)

class PostRequest(BaseRequest):
    def post(self, endpoint, data=None, json=None):
        return super().send_request('POST', endpoint, data=data, json=json)

class PutRequest(BaseRequest):
    def put(self, endpoint, data=None, json=None):
        return super().send_request('PUT', endpoint, data=data, json=json)

# 使用示例
if __name__ == "__main__":
    base_url = "http://preapi.smartbike.xiaoantech.com"
    get_request = GetRequest(base_url)
    post_request = PostRequest(base_url)
    put_request = PutRequest(base_url)

    # 发送GET请求
    response = get_request.get("/java/led/application/v1/app/user/activities", params={"lng": "114.43499050564236","city":"武汉市","lat":"30.500406629774307"})
    print(response)

    # 发送POST请求
    # response = post_request.post("/path/to/resource", json={"key": "value"})
    # print(response)


