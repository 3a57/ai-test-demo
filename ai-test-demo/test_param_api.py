# test_param_api.py
import pytest # 单元测试框架
import requests # HTTP客户端库

# 使用内置装饰器传入多组参数
@pytest.mark.parametrize("post_id, expected_keyword",[
    (1,"sunt aut"),
    (2,"qui est"),
    (3,"ea molestias"),
    (4,"eum et est")  #可再继续添加测试数据
    ])
def test_post_title(post_id, expected_keyword):
    # 验证不同ID的文章标题是否包含预期关键词
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    resp = requests.get(url)

    # 断言
    assert resp.status_code == 200, f"ID={post_id} 返回状态码{resp.status_code}"

    data = resp.json()
    assert data["id"] == post_id, f"返回的ID不匹配：{data['id']}"

    assert expected_keyword in data["title"], f"ID={post_id}的标题应该包含'{expected_keyword}',实际：{data['title']}"