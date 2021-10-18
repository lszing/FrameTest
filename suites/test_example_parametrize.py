##参数化例子
import pytest
# import pyyaml
from util.readYaml import ReadYaml


# yamldata=[1,2,3]
# def sum(x, y):
#     z = x + y
#     return z
def sum(x, y):
    z = x + y
    return z

class Test_parametrize:
    yamldata=ReadYaml().readYaml('/data/test.yaml')

    # def setup(self):
    #     yamldata=self.r.readYaml('/data/test.yaml')


    # def test_1(self,dict1):
    def fs(self,dict1):
        print(dict1)
        assert sum(dict1[0],dict1[1])==dict1[2]
        def wap(func):
            func()
        return wap





    # r = ReadYaml()
    # r.readYaml('data\test.yaml')
    # print(r)
    # pytest.main(['-s','suites/test_example_parametrize','--alluredir','./temp'])
        