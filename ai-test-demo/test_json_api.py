# test_json_api.py
import requests # 导入HTTP客户端库

def test_get_post_by_id_1():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url) # 获取响应信息

    # 验证状态码
    assert response.status_code == 200,f"Expected 200,got {response.status_code}"

    # 解析json:只包含服务器返回的json数据内容，不包含HTTP状态码
    data = response.json()

    # 验证字段
    assert data["id"] == 1,"Post id should be 1"
    assert "sunt aut" in data["title"],"Title should contain 'sunt aut'"
    assert len(data["body"]) > 10,"Body should not be too short"

    # print("✅ Test passed: Post ID=1 verified")

# if __name__ == "__main__":
#     test_get_post_by_id_1()