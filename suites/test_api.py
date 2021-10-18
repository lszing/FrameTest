import pytest
from suites.tbase import TBase
from util.readJson import ReadJson
from log.logpro import log


class Test(TBase):

    # data=[{'api_test': {'url': 'aaa', 'params': {'order_no': 'order_no', 'amount': 'amount', 'return_url': 'return_url', 'trans_id': 'trans_id'}, 'headers': {'fddf': '123'}}}]
    # 坑：想用parametrize传一个字典必须要把字典append到一个列表中 因此在readJson中append了一下

    # 两种用字符串调用类方法的方法
    # a='Api_test().process'
    # eval(a)('data')
    # c_str = eval(scene)(data)
    # print('eval=======',c_str)
    # api=getattr(c_str,'process')()

    # # todo 与filter逻辑不匹配 暂时不用
    # @pytest.mark.parametrize('data', data)

    def to_do(self):
        print("todo")
    # def test_3(self, data):
    #     log.info(f"data is{data}")
    #     super(Test, self).scene_work(data)

if __name__ == '__main__':
    # 执行pytest会先去父类里找test开头的文件
    # pytest.main(['-s', 'test_api.py', '--alluredir', './temp'])
    # pytest.main(['-s', '-q','--filter=sweqrqwe','test_api.py'])
    pytest.main('-v -s  --filter case1  --path test test_api.py --cache-show')
    # pytest.main(['-v', '-s'  '-filter=case1',  '--path=test', 'test_api.py '])
    # pytest.main(['-s', 'suites/taddoptsest_example_testinherit', '--alluredir', './temp'])
