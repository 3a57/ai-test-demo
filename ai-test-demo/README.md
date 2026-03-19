# AI Test Demo Project

## Day 1 Goal
- 搭建 Python 测试环境
- 使用 requests 调用公开 API

## 如何运行
1. `python -m venv venv`
2. `source venv/bin/activate` (Linux/Mac) 或 `venv\Scripts\activate` (Windows)
3. `pip install -r requirements.txt`
4. `python test_demo_api.py`


- Day 2: `python test_json_api.py` — 验证 JSONPlaceholder API 字段


# Day3
## 如何运行测试
```bash
pip install -r requirements.txt
pytest  ----目前还是使用python -m pytest运行 待配置

- Day 4: `test_param_api.py` — 使用 @pytest.mark.parametrize 测试多组数据