# utils/http_client.py
# 导入HTTP客户端库
import requests 

def get(url,headers=None):
    # 发送GET请求
    response = requests.get(url, headers=headers)
    return response

def post(url,headers=None):
    # 发送POST请求
    response = requests.post(url,headers=headers)
    return response

