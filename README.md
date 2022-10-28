## 框架支持的功能可查看demo
- suites/test_demo.py  用例维度数据  
- api/api_demo.py   接口维度接口数据及接口参数逻辑
- 执行单条case pytest -vs --filter="用例名" ./suites/api_demo.py
- 执行文件下全部case  pytest -vs  ./suites/api_demo.py
- 执行suites下全部测试文件 pytest -vs ./suites
- 测试报告用的pytest-html,conftest中重写钩子函数增加用例描述和错误信息