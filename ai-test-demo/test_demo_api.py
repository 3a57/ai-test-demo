# test_demo_api.py
# 从另一个文件导入函数
from utils.http_client import get

def test_httpbin_get():
    url = "https://httpbin.org/get"
    response = get(url)
    print("Status Code:",response.status_code)
    print("Response Josn:")
    print(response.json())

if __name__ == "__main__":
    test_httpbin_get()