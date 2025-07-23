# -*- coding: utf-8 -*-
"""
@Author  : XIAOAN
@Time    : 2025/2/11 21:45
@File    : testscript.py
@Description :
@progname: xz_api_auto
"""
# import configparser
# import requests
#
# response = requests.request(method='POST',
#                             url='http://preapi.smartbike.xiaoantech.com/java/led/application/v1/app/login/extends',
#                             json={
#                                     "phone":"13700042744",
#                                     "idCardNo":"42500022744",
#                                     "username":"坤拳42744"
#                                     },
#                             headers={"content-type":"application/json","xflag":"eGlhb2dlY2xpZW50OjEyMzQ1Ng=="}
#                             )
#
# # print(response.json(),"*********\n")
# #
# getstring = response.json()["data"]["signKey"]
# print(getstring)

# config = configparser.ConfigParser()
# config.read('/config.ini')
# config['otherparams']["userid"] = f'{getstring}'
# with open('../config.ini', 'w') as configfile:
#     config.write(configfile)

import pandas as pd
import requests

# 1. 读取 Excel 文件
file_path = './data.xlsx'  # Excel 文件路径
df = pd.read_excel(file_path)

# 2. 定义处理函数（例如发送 HTTP 请求）
def process_data(row):
    """
    根据 A、B、C 列的数据进行处理，并返回结果
    """
    # 示例：假设 A、B、C 列分别是参数 1、参数 2、参数 3
    param1 = row['phone']
    param2 = row['idCardNo']
    param3 = row['username']

    # 示例：发送 HTTP 请求（假设是一个 POST 请求）
    # url = 'http://preapi.smartbike.xiaoantech.com/java/led/application/v1/app/login/extends'  # 替换为实际的 API 地址
    # payload = {
    #             "phone":f"{param1}",
    #             "idCardNo":f"{param2}",
    #             "username":f"{param3}"
    #             },
    # headers={"content-type":"application/json","xflag":"eGlhb2dlY2xpZW50OjEyMzQ1Ng=="}
    try:
        response =requests.request(method='POST',
                            url='http://preapi.smartbike.xiaoantech.com/java/led/application/v1/app/login/extends',
                            json={
                                    "phone":f"{param1}",
                                    "idCardNo":f"{param2}",
                                    "username":f"{param3}"
                                    },
                            headers={"content-type":"application/json","xflag":"eGlhb2dlY2xpZW50OjEyMzQ1Ng=="}
                            )
        response.raise_for_status()  # 检查请求是否成功
        print(response.text)
        result = response.json()["data"]["signKey"]
        print(result)
    except requests.exceptions.RequestException as e:
        result = f"Error: {e}"  # 如果请求失败，记录错误信息

    return result

def process_SN(row):
    """
    根据 A、B、C 列的数据进行处理，并返回结果
    """
    # 示例：假设 A、B、C 列分别是参数 1、参数 2、参数 3
    token = row['token']
    try:
        response =requests.request(method='GET',
                            url='http://preapi.smartbike.xiaoantech.com/java/led/application/v1/app/user/detail',
                            params='',
                            headers={
                                    "traceid" : "147258369147258369159",
                                    "authorization" : f"{token}",
                                    "xFlag" : "eGlhb2dlY2xpZW50OjEyMzQ1Ng==",
                                    "content-type" : "application/json",
                                    "appfrom" : "zfb",
                                    "appid" : "2021003175692262",
                                    "citypinyin" : "wuhanshi"
                                    }
                            )
        response.raise_for_status()  # 检查请求是否成功
        print("响应内容：：：",response.text)
        cabinetimei = response.json()["data"]["batteryNo"]
        print("电柜SN：：：",cabinetimei)
    except requests.exceptions.RequestException as e:
        cabinetimei = f"Error: {e}"  # 如果请求失败，记录错误信息
    tmpsn = cabinetimei[9:24]
    cabinetsn = '20202400' + tmpsn[-2:]
    return cabinetsn

# 2. 读取 token 并修改 config.ini

# 3. 从第一行开始，循环处理每一行数据
index = 1
for index, row in df.iterrows():
    # 调用处理函数，获取结果
    result = process_data(row)
    # cabinetsn = process_SN(row)
    # 将结果写入 D 列
    df.at[index, 'token'] = result
    # df.at[index,'cabinetimei'] = cabinetimei
    # df.at[index,'cabinetsn'] = cabinetsn

# 4. 保存修改后的 Excel 文件
output_file_path = './data.xlsx'  # 输出文件路径
df.to_excel(output_file_path, index=False)

print(f"处理完成，结果已保存到 {output_file_path}")