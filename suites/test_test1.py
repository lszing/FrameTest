import pytest
from suites.tbase import TBase
from util.readJson import ReadJson
from log.logpro import log


class Test(TBase):
    def test(self):
        data = {
            "case1": {
                "info": "",
                "stepList": {
                    "1": {
                        "scene": "skuDetail",
                        "assert": {
                            "response": {
                                "<withkeys>": "code"
                            }
                        }
                    },
                    "2": {
                        "scene": "skuDyInfo",
                        "params": {
                            "body.skuId0": "1.skuDetail.response.wareInfo.basicInfo.wareId",

                            "body": {
                                "skuId": "1.skuDetail.response.wareInfo.basicInfo.wareId",
                                "skuId1": "1.skuDetail.response.wareInfo.basicInfo.wareId"
                            },

                            "body.skuId3.test1": {
                                "test2": "1.skuDetail.response.wareInfo.basicInfo.wareId",
                                "test3": "1.skuDetail.response.wareInfo.basicInfo.wareId"
                            }
                        },
                        "assert": {
                            "response": {
                                "<withkeys>": "code"
                            }
                        }
                    }
                }
            }
        }
        return super(Test,self).test_scene_work(data['case1'])

if __name__ == '__main__':
    # 执行pytest会先去父类里找test开头的文件
    # pytest.main(['-s', 'test_api.py', '--alluredir', './temp'])
    # pytest.main(['-s', '-q','--filter=sweqrqwe','test_api.py'])
    pytest.main('-v -s  --filter case1  --path test test_api.py --cache-show')
    # pytest.main(['-v', '-s'  '-filter=case1',  '--path=test', 'test_api.py '])
    # pytest.main(['-s', 'suites/taddoptsest_example_testinherit', '--alluredir', './temp'])
