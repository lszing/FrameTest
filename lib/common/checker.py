import json
import re
import copy
from log.logpro import log
from util.readJson import ReadJson
from util.util_common import util_common
import traceback


class Checker(object):
    method_map = {
        'response': 'check_point',
        'db': '',
        'redis': '',
    }
    rule_map = {
        "notnull": "checkNotNull",
        "null": "checkNull",
        "typeequal": "checkTypeEquals",
        "notequal": "checkNotEquals",
        "withkeys": "checkArrayHasKeys",
        "elementscount": "checkArrayElementsCount",
        "withoutkeys": "checkWithoutKeys",
        "regexmatch": "checkStringRegexMatch",
        "inarray": "checkContainsInArray",
        "checktype": "checkTypeOnly",
        "containsubset": "checkContainsSubset",
    }
    type_list = ["int", "str", "float", "list", "tuple", "dict", "set"]

    def __init__(self, except_data, actual_data):
        self.except_data = except_data
        self.actual_data = actual_data

    def check(self):
        # 最外层判断 校验相应，db，redis  todo  目前只有response 对应的check_point
        for key, value in self.except_data.items():
            try:
                met = self.method_map[key]
            except:
                log.warning(f'key {key} is not in mehtod_map {self.method_map}')
                raise AssertionError(f'key {key} is not in mehtod_map {self.method_map}')
                # return False
            result = getattr(self, met)(value)
            # result = met(value)
            if result == False:
                raise AssertionError
            else:
                return True

    def check_point(self, except_data):
        # 判断是字典
        if isinstance(except_data, dict):
            for key, value in except_data.items():
                # 判断正则<***> 调用各个方法
                if re.match(r'^\<[A-Za-z]+\>$', key):
                    # 通过正则
                    func = self.get_rule(key)
                    try:
                        # result = getattr(self, func)(value, self.actual_data)
                        getattr(self, func)(value, self.actual_data)
                    except Exception as e:
                        # print(repr(e))
                        # traceback.format_exc()
                        log.fatal(f"file {e.__traceback__.tb_frame.f_globals['__file__']} {e.__traceback__.tb_lineno} {e}")
                        log.fatal(f'method {func} check fail')
                        return False
                    # if result == False:
                    #     raise "异常，未到校验逻辑"
                    # else:
                    log.info('case check success!')
                # 不符合正则 则认为是正常字段做==校验
                # python3已经从删除dict.has_key()方法
                # elif value and key in self.actual_data:
                elif value:
                    try:
                        assert value == self.actual_data[key]
                        print(f"except_data=[ {key}={value} ], actual_data={self.actual_data} check success")
                    except:
                        # log.fatal(f"except_data={value} \n, actual_data={json.dumps(self.actual_data,indent=4)}")
                        log.fatal(f"except_data=[ {key}={value} ], actual_data={self.actual_data}")
                        return False
                #  eg: message.data.amount
                elif len(key.split('.')) > 1:
                    tmp_actual_data = copy.deepcopy(self.actual_data)
                    key_list = key.split('.')
                    for i in range(len(key_list)):
                        try:
                            # 实际结果
                            tmp_actual_data = tmp_actual_data[key_list[i]]
                        except:
                            log.fatal(f'key {key_list[i]} is not in actual_data={tmp_actual_data}')
                            return False
                    # 判断成功
                    if tmp_actual_data == value:
                        return True
                    else:
                        log.fatal(f'except {key}={value} ,actual {tmp_actual_data} is not eqaul')
                        return False
            return True

    def get_rule(self, key):
        key = key[1:len(key) - 1]
        # print(str.upper())  # 把所有字符中的小写字母转换成大写字母
        # print(str.lower())  # 把所有字符中的大写字母转换成小写字母
        # print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
        # print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写
        func = self.rule_map[key.lower()]
        return func

    # 校验不空  done
    # 这里传进来的except_data为'<notnull>'的值
    # "<notnull>": {
    #               "data": {
    #                 "content": ["sp_no","amount"]
    #               }
    #             }, 验证通过
    def checkNotNull(self, except_data, actual_data):
        # 递归获取数据
        result_dict = util_common().recursive(except_data, actual_data)
        # if result_dict:
        check_data = {}
        for key, value in result_dict['except_data'].items():
            try:
                if isinstance(value, list):
                    for i in range(len(value)):
                        check_data[value[i]] = result_dict['actual_data'][key][value[i]]
                else:
                    check_data[key] = result_dict['actual_data'][key][value]
            except:
                log.fatal(
                    f'get data fail ,key=\' {value} \' is not in actual_data={actual_data}  ')
                raise AssertionError
            log.info(
                f"start checkNotNull,except_data=={result_dict['except_data']},actual_data={result_dict['actual_data']}")
            for j in check_data:
                assert check_data[j] != '' and check_data[j] is not None
            print(
                f" except_data=={except_data} is not None,actual_data={result_dict['actual_data'][key]} assert success")
        # else:
        # 进入else则认为未取到key 既校验失败
        # return False
        #     raise AssertionError

    # 判断字段为空 传进来的为'<null>' 逻辑与不空相同 支持列表
    def checkNull(self, except_data, actual_data):
        result_dict = util_common().recursive(except_data, actual_data)
        if result_dict:
            if isinstance(result_dict['except_data'], list):
                for i in result_dict['except_data']:
                    log.info(f"checkNull except_data is {i} ")
                    assert result_dict['actual_data'][i] == '' or result_dict['actual_data'][i] is None
            else:
                assert result_dict['actual_data'][result_dict['except_data']] == '' or result_dict['actual_data'][
                    result_dict['except_data']] is None
        else:
            # 进入else则认为未取到key 既校验失败
            return False

    # 判断类型相同   done
    # def checkTypeEquals(self, except_data, actual_data):
    #     result_dict = util_common().recursive(except_data, actual_data)
    #     for key, value in result_dict['except_data'].items():
    #         try:
    #             check_data = result_dict['actual_data'][key]
    #         except:
    #             log.fatal(
    #                 f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}  ')
    #             raise AssertionError
    #         log.info(f"start checkNotNull,except_data=={except_data},actual_data={result_dict['actual_data']}")
    #         assert isinstance(check_data, eval(value))
    #
    #         print(f" assert success")



    #根据期望数据获取实际结果
    def get_check_data(func):
        def wrapper(self, except_data, actual_data):
            result_dict = util_common().recursive(except_data, actual_data)
            for key, value in result_dict['except_data'].items():
                try:
                    check_data = result_dict['actual_data'][key]
                except:
                    log.fatal(
                        f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}')
                    raise AssertionError(f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}')
                log.info(f"start check {func},except_data=={except_data},actual_data={result_dict['actual_data']}")
                func(self, value, check_data)

        return wrapper

    #判断类型相同  10.11 done
    @get_check_data
    def checkTypeEquals(self, except_data, actual_data):
        if except_data not in self.type_list:
            raise TypeError(f"except_data type {except_data} not in type_list{self.type_list}")
        assert isinstance(actual_data,eval(except_data))
    # 判断不相等 测试完成9.30
    @get_check_data
    def checkNotEquals(self, except_data, actual_data):
        assert except_data != actual_data

    # 判断返回json包含key  测试完成  "<withkeys>": {
    # "data": {
    #   "content": ["sp_no1","amount"]
    # }      9.30done
    @get_check_data
    def checkArrayHasKeys(self, except_data, actual_data):
        if isinstance(except_data, list):
            for i in range(len(except_data)):
                assert except_data[i] in actual_data.keys() ,f"checkArrayHasKeys fail except_data={except_data[i]} not in actual_data={actual_data.keys()}"
        else:
            assert except_data in actual_data.keys()

    # 判断返回json不包含key   9.30done
    # "<withoutkeys>": {
    #     "data": {
    #         "content": ["test", "sp_no"]
    #     }
    # }
    @get_check_data
    def checkWithoutKeys(self, except_data, actual_data):
        print('ex', except_data)
        print('ac', actual_data)
        if isinstance(except_data, list):
            for i in range(len(except_data)):
                assert except_data[i] not in actual_data.keys()
        else:
            assert except_data not in actual_data.keys()

    # 判断返回json中包含元素的数量  done 9.30
    @get_check_data
    def checkArrayElementsCount(self, except_data, actual_data):
        print('ex', except_data)
        print('ac', actual_data)
        assert except_data == len(actual_data.keys())

    #正则匹配校验 入参直接返回 字段值 不包括键名  9.30done  无法校验正则本身正确性
    @get_check_data
    def checkStringRegexMatch(self, except_data, actual_data):
        assert re.match(except_data, actual_data)



if __name__ == '__main__':
    pass
    # if re.match(r'^\<[A-Za-z]+\>$', '<mathch>'):
    #     print('1')
    # else:
    #     print('2')
    # data = ReadJson('test1').readJson()
    #
    # except_data = data[0]['except_data']['response']
    # actual_data = data[1]['actual_data']['response']
    # Checker(except_data, actual_data).check_point(except_data)
    # a = '1231241'
    # b = 'str'
    # assert isinstance(a, eval(b))
