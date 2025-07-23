# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/17 22:37
@File    : lianxi001.py
@Description : 
@progname: xz_api_auto	
"""
import os.path
import pathlib
from pathlib import Path

# import pandas
#
# file_path = './data.xlsx'
# df = pandas.read_excel(file_path)
#
# index = 0
#
# for index,item in  df.iterrows():
#
#     if index == 5:
#         break
#     print(index, "\n", item)
#     print(item["phone"])
#     print(type(item))


# # 创建一个 Series
# s = pd.Series([1, 3, 5, 7, 9])
# print(s)
#
# # 创建一个 DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
#
# df = pd.DataFrame(data)
# print(df)
# #
# # df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
# # df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})
# #
# # result = pd.concat([df1, df2])
# # print(result)



# import requests
#
# # 文件的 URL
# url = 'https://xc-led.oss-cn-hangzhou.aliyuncs.com/exportFiles/2b6b929190513d9ca644a04ea2920920/用户报表-20250305145358.xlsx'
#
# # 发送 HTTP GET 请求
# response = requests.get(url, stream=True)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     # 设置本地保存路径
#     local_filename = url[-24:]
#
#     # 以二进制写入模式打开文件
#     with open(local_filename, 'wb') as file:
#         # 分块写入文件，避免大文件占用过多内存
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)
#     print(f"文件已下载到: {local_filename}")
# else:
#     print(f"下载失败，状态码: {response.status_code}")

# abc = 'https://xc-led.oss-cn-hangzhou.aliyuncs.com/exportFiles/2b6b929190513d9ca644a04ea2920920/用户报表-20250305145358.xlsx'
#
# print(abc[-24:])

# local_filename = os.path.dirname(os.path.abspath(__file__)) + '..\\' + '..\\' + 'wang.xlsx'
# abc = pathlib.Path(__file__).parent.parent.absolute() / 'test_data' / 'wang.xlsx'
#
# print(local_filename)
# print(abc)
# print(type(abc))

from urllib.parse import quote

encoded = quote("换电记录", encoding='utf-8')
print(encoded)