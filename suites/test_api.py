import pytest
from suites.tbase import TBase
from util.json_util import ReadJson
from log.logpro import log


class Test_api1(TBase):
    # 两种用字符串调用类方法的方法
    # a='Api_test().process'
    # eval(a)('data')
    # c_str = eval(scene)(data)
    # print('eval=======',c_str)
    # api=getattr(c_str,'process')()

    # 与filter逻辑不匹配 暂时不用
    # @pytest.mark.parametrize('data', data)
    pass


if __name__ == '__main__':
    # pytest.main(['-s', 'test_api.py', '--alluredir', './temp'])
    # pytest.main(['-s', '-q','--filter=sweqrqwe','test_api.py'])
    pytest.main('-v -s   test_api.py --cache-show')
    # pytest.main(['-v', '-s'  '-filter=case1',  '--path=test', 'test_api.py '])
    # pytest.main(['-s', 'suites/taddoptsest_example_testinherit', '--alluredir', './temp'])
