import pytest
import allure
import os
#-n 多线程 2 两个线程
#pytest.main(['-s','suites/test_example.py','-n','2'])
#将本次运行结果放入./temp文件夹内
pytest.main(['-s','suites/test_api.py','--alluredir','./temp'])
# os.system('allure generate ./temp -o ./report --clean')