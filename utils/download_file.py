# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/3/5 15:05
@File    : download_file.py
@Description : 
@progname: xz_api_auto	
"""
import os.path
import pathlib
from pathlib import Path

import requests

from common.getsignKey import GetSysSignKey, sysLogin_message
from utils.logger import logger

def download_excel(file_path,filename,):
    # 发送 HTTP GET 请求
    response = requests.get(file_path, stream=True)
    print("这是在被调用++++++++++++++++++++++“”“”“”“”“”“”“")
    # 检查请求是否成功
    if response.status_code == 200:
        # 设置本地保存路径
        local_filename = pathlib.Path(__file__).parent.parent.absolute() / 'test_data' /  filename

        # 以二进制写入模式打开文件
        with open(local_filename, 'wb') as file:
            # 分块写入文件，避免大文件占用过多内存
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        logger.info(f"文件已下载到: {local_filename}")
    else:
        logger.info(f"下载失败，状态码: {response.status_code}")

# getSystemSignKey = GetSysSignKey()
# getSystemSignKey.save_sysToken_to_config(getSystemSignKey.getSysToken(sysLogin_message))
# secret = getSystemSignKey.load_sysToken_from_config()
# url = 'http://preapi.smartbike.xiaoantech.com/java/led/system/v1/platform/excel/exportList'
# headers = {
# 	"Accept":"application/json, text/plain, */*",
# 	"Accept-Encoding":"gzip, deflate",
# 	"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
# 	"Connection":"keep-alive",
# 	"Content-Type":"application/json;charset=UTF-8",
# 	"User-Agent":"Mozilla/5.0 (Linu x; Android 14; PHM110 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300289 MMWEBSDK/20241103 MMWEBID/490 MicroMessenger/8.0.5 4.2760(0x28003653) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
# 	"Authorization":secret
# 	}
#
# response = requests.get(url=url, params={"pageSize": "50", "pageNum": "1", "fileType": "10"}, headers=headers)
# subDir = response.json()['data']['list'][0]["subDir"]
# file_name = response.json()['data']['list'][0]["name"]
# file_path = 'https://xc-led.oss-cn-hangzhou.aliyuncs.com/exportFiles/' + subDir + '/' + '%E7%94%A8%E6%88%B7%E6%8A%A5%E8%A1%A8' + file_name[-20:]
#
# download_excel(file_path,file_name)