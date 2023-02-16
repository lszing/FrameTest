import pytest

from suites.tbaseNew import TBaseNew


class Test_demo(TBaseNew):
    case_data = {
        "case1": {
            "info": "用例描述",
            "stepList": {
                # 用例第一步
                "1": {
                    # 对应接口类名
                    "scene": "api1",
                    # query参数
                    "params": {
                        "param1": "1"
                    },
                    # 请求体数据
                    "body": {
                        "请求体参数": "1"
                    },
                    # 请求体字符串
                    "bodyStr": '''123123123''',
                    # 请求头参数
                    "headers": {
                        "header1": "1"
                    },
                    # 断言内容
                    "assert": {
                        # 响应结果校验
                        "response": {
                            # 校验等于
                            "code": "SUCCESS",
                            # 校验不空 data下content下sp_no,amount不为空
                            "<notnull>": {
                                "data": {
                                    "content": ["sp_no", "amount"]
                                }
                            },
                            # 校验为空 与notnull逻辑相同
                            "<null>": {
                                "data": {
                                    "content": ["sp_no", "amount"]
                                }
                            },
                            # 校验类型相同 c
                            "<typeequal>": {
                                "data1": "类型如：str/int"
                            },
                            # 校验不相等 data1!=1
                            "<notequal>": {
                                "data1": "1"
                            },
                            # 校验存在key data下content下sp_no1,amount存在
                            "<withkeys>": {
                                "data": {
                                    "content": ["sp_no1", "amount"]
                                }
                            },
                            # 校验元素数量 data下content list下元素的数量
                            "<elementscount>": {
                                "data": {
                                    "content": 3
                                }
                            },
                            # 校验存在key data下content下sp_no1,amount不存在
                            "<withoutkeys>": {
                                "data": {
                                    "content": ["sp_no1", "amount"]
                                }
                            },
                            # 校验正则 正则用户自己写 译为 content的value是否符合正则
                            "<regexmatch>": {
                                "data": {
                                    "content": "正则表达式"
                                }
                            },
                            # 校验值存在
                            # 字典中多个key且值不确定在哪个key中，规范格式key=data.content.*.order_no 其中*为多重key
                            "<existvalue>": {
                                "data.paymentMethods.*.paymentMethod": "IOUP",
                                "data.data1.data2": "data3"
                            },
                            # 校验值不存在
                            # 同上
                            "<existnotvalue>": {
                                "data.paymentMethods.*.paymentMethod": "IOUP",
                                "data.data1.data2": "data3"
                            }
                        },
                    },
                    # db校验
                    "db": {
                        "tableName1": {
                            "column1": "期望数据1",
                            "column2": "期望数据2"
                        },
                        "tableName2": {
                            "column3": "期望数据1",
                            "column4": "期望数据2"
                        }
                    }
                }
            },
            # 用例第二步
            "2": {
                "scene": "api2",
                "params": {
                    # 获取之前步骤的请求数据 step.scene.request/
                    "params1": "1.api1.request.params.param1",

                    # 多维json获取之前步骤的数据写法

                    "body.param1": "step.scene.response.key1.key2.value",
                    # 处理后参数格式为：body:{"param1":动态数据}

                    "body": {
                        "param1": "step.scene.response.key1.key2.value",
                        "param2": "step.scene.response.key1.key2.value"
                    },
                    # 处理后参数格式为：body:{"param1":动态数据1,"param2":动态数据2}

                    "body.param1.param2": {
                        "param3": "step.scene.response.key1.key2.value",
                        "param4": "step.scene.response.key1.key2.value"
                    }
                    # 处理后参数格式为：body:{"param1":{"param2":{"param3":动态数据1,"param4":动态数据2}}}
                },
                # 断言内容
                "assert": {
                    # 响应结果校验
                    "response": {
                        # 获取之前步骤的响应数据
                        "code": "1.api1.response.code",
                        "header": "1.api1.response.header",
                    },
                    # db校验
                    "db": {
                        "tableName1": {
                            "column1": "期望数据1",
                            "column2": "期望数据2"
                        },
                        "tableName2": {
                            "column3": "期望数据1",
                            "column4": "期望数据2"
                        }
                    }
                }
            }
        }
    }

    if __name__ == '__main__':
        pytest.main(['-vs', '--filter=case5', '.\suites\Test_refundcallback.py'])
