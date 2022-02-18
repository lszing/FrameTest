import json
import re
import copy
from log.logpro import log
from util.json_util import ReadJson
from util.util_common import util_common
import traceback
from util.util_redis import redisManager

indent = '\n--------------------------------------------------------------------------\n'


def get_check_data(func):
    def wrapper(except_data, actual_data):
        result_dict = util_common().recursive(except_data, actual_data)
        for key, value in result_dict['except_data'].items():
            try:
                check_data = result_dict['actual_data'][key]
            except:
                log.fatal(
                    f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}')
                raise AssertionError(f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}')
            log.info(f"start check {func},except_data:{except_data},actual_data:{result_dict['actual_data']}")
            print(
                f"start check {func}{indent}except_data:{except_data}{indent}actual_data:{result_dict['actual_data']}")
            func(value, check_data)

    return wrapper


class Checker(object):
    method_map = {
        'response': 'check_point',
        'db': 'check_redis',
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
        "existvalue": "checkValueIsExist",  # 字典中多个key且值不确定在哪个key中，规范格式要求data.content.*.order_no 其中*为多重key
        "existnotvalue": "checkValueNotExist",  # 同上
        "inarray": "checkContainsInArray",
        "checktype": "checkTypeOnly",
        "containsubset": "checkContainsSubset",
    }
    type_list = ["int", "str", "float", "list", "tuple", "dict", "set"]

    def __init__(self, except_data, actual_data, redis_conf=None, db_conf=None):
        self.except_data = except_data
        self.actual_data = actual_data
        self.redis_conf = redis_conf
        self.db_conf = db_conf

    def check(self):
        all_result = True
        # 最外层判断 校验相应，db，redis  todo  目前只有response 对应的check_point
        for key, value in self.except_data.items():
            try:
                met = self.method_map[key]
            except:
                log.warning(f'key {key} is not in mehtod_map {self.method_map}')
                raise AssertionError(f'key {key} is not in mehtod_map {self.method_map}')
            all_result = getattr(self, met)(value)

            # if result == False:
            #     raise AssertionError
            # else:
            #     return True
        if all_result != False:
            return True

    def check_point(self, except_data):
        # 判断是字典
        if isinstance(except_data, dict):
            for key, value in except_data.items():
                # 判断正则<***> 调用各个方法
                if re.match(r'^\<[A-Za-z]+\>$', key):
                    # 通过正则
                    func = self.get_rule(key)
                    # todo 10.26 优化校验结果逻辑 可能改回来
                    # try:
                    # result = getattr(self, func)(value, self.actual_data)
                    getattr(self, func)(value, self.actual_data)
                    # except Exception as e:
                    #     # print(repr(e))
                    #     # traceback.format_exc()
                    #     log.fatal(
                    #         f"file {e.__traceback__.tb_frame.f_globals['__file__']} {e.__traceback__.tb_lineno} {e}")
                    #     log.fatal(f'method {func} check fail')
                    #     return False
                    # if result == False:
                    #     raise "异常，未到校验逻辑"
                    # else:
                    log.info('case check success!')
                # 不符合正则 则认为是正常字段做==校验
                # python3已经从删除dict.has_key()方法
                # elif value and key in self.actual_data:
                elif len(key.split('.')) > 1:
                    tmp_actual_data = copy.deepcopy(self.actual_data)
                    key_list = key.split('.')
                    for i in range(len(key_list)):
                        try:
                            # 实际结果
                            if key_list[i].isdigit():
                                num = int(key_list[i])
                                tmp_actual_data = tmp_actual_data[num]

                            else:
                                tmp_actual_data = tmp_actual_data[key_list[i]]

                        except:
                            log.fatal(f'key [{key_list[i]}] is not in actual_data:{tmp_actual_data}')
                            raise AssertionError(f'key [{key_list[i]}] is not in actual_data:{tmp_actual_data}')
                    # 判断成功
                    try:
                        assert tmp_actual_data == value
                        print(
                            f'{indent}except_data:[{key}={value},type:{type(value)}]{indent}actual_data:[{key}={tmp_actual_data},type:{type(value)}]{indent}check success! ')
                    except:
                        log.fatal(
                            f"\nexcept_data:[{key}={value},type:{type(value)}]{indent}actual_data:[{key}={tmp_actual_data},type:{type(value)}]{indent}check Fail")
                        # print(
                        #     f"except_data:[{key}={value},type:{type(value)}]{indent}actual_data:[{key}={tmp_actual_data},type:{type(value)}]{indent}check Fail")
                        raise AssertionError(
                            f'{indent}except_data:[{key}={value},type:{type(value)}]{indent}actual_data:[{key}={tmp_actual_data},type:{type(value)}] {indent}\033[30;41;1m not equal,check fail \033[0m')
                else:
                    try:
                        assert value == self.actual_data[key]
                        print(
                            f"except_data:[{key}={value},type:{type(value)}]{indent}actual_data:[{key}={self.actual_data[key]},type:{type(self.actual_data[key])}]{indent}\033[32;1m check success \033[0m")
                    except:
                        log.fatal(
                            f"except_data:[{key}={value},type:{type(value)}], actual_data:[{key}={self.actual_data[key]},type:{type(self.actual_data[key])}]")
                        print(
                            f"except_data:[{key}={value},type:{type(value)}]{indent}actual_data:[{key}={self.actual_data[key]},type={type(self.actual_data[key])}]{indent}check Fail")
                        raise AssertionError(
                            f"except_data:[{key}={value},type:{type(value)}],actual_data:[{key}={self.actual_data[key]},type={type(self.actual_data[key])}],check Fail")
                #  eg: message.data.amount
            return True

    def check_redis(self, redis_except_data):
        redis_manager = redisManager(self.redis_conf)
        for k, v in redis_except_data.items():
            for key, value in v.items():
                assert getattr(redis_manager, 'get_' + k[1:-1])(key) == value

        # if '<string>' in redis_except_data.keys():
        #     for k, v in redis_except_data['<string>'].items():
        #         assert redis_manager.get_key(k) == v
        # if '<map>' in redis_except_data.keys():
        #     for k, v in redis_except_data['<map>'].items():
        #         assert redis_manager.get_map(k) == v
        # if '<list>' in redis_except_data.keys():
        #     for k, v in redis_except_data['<list>'].items():
        #         assert redis_manager.get_list(k) == v
        # if '<set>' in redis_except_data.keys():
        #     for k, v in redis_except_data['<set>'].items():
        #         assert redis_manager.get_set(k) == v

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
                raise AssertionError(f'get data fail,[key={value}] is not in [actual_data={actual_data}]')
            log.info(
                f"start checkNotNull,except_data=={result_dict['except_data']},actual_data={result_dict['actual_data']}")
            for j in check_data:
                assert check_data[j] != '' and check_data[j] is not None
            print(
                f"except_data is {except_data} is not None{indent}actual_data={result_dict['actual_data'][key]}{indent}assert success")

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

    # 根据期望数据获取实际结果
    # def get_check_data(func):
    #     def wrapper(self, except_data, actual_data):
    #         result_dict = util_common().recursive(except_data, actual_data)
    #         for key, value in result_dict['except_data'].items():
    #             try:
    #                 check_data = result_dict['actual_data'][key]
    #             except:
    #                 log.fatal(
    #                     f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}')
    #                 raise AssertionError(f'get data fail ,key=\' {key} \' is not in actual_data={actual_data}')
    #             log.info(f"start check {func},except_data:{except_data},actual_data:{result_dict['actual_data']}")
    #             print(
    #                 f"start check {func}{indent}except_data:{except_data}{indent}actual_data:{result_dict['actual_data']}")
    #             func(self, value, check_data)
    #
    #     return wrapper

    # 判断类型相同  10.11 done
    @get_check_data
    def checkTypeEquals(self, except_data, actual_data):
        if except_data not in self.type_list:
            raise TypeError(f"except_data type {except_data} not in type_list{self.type_list}")
        assert isinstance(actual_data, eval(except_data))

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
                assert except_data[
                           i] in actual_data.keys(), f"checkArrayHasKeys fail except_data={except_data[i]} not in actual_data={actual_data.keys()}"
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
        if isinstance(except_data, list):
            for i in range(len(except_data)):
                assert except_data[i] not in actual_data.keys()
        else:
            assert except_data not in actual_data.keys()

    # 判断返回json中包含元素的数量  done 9.30
    @get_check_data
    def checkArrayElementsCount(self, except_data, actual_data):
        if isinstance(actual_data, dict):
            assert except_data == len(actual_data.keys())
        elif isinstance(actual_data, list):
            assert except_data == len(actual_data)

    # 正则匹配校验 入参直接返回 字段值 不包括键名  9.30done  无法校验正则本身正确性
    @get_check_data
    def checkStringRegexMatch(self, except_data, actual_data):
        assert re.match(except_data, actual_data)

    def for_check_value(self, except_data, actual_data):
        index = 0
        key_list = []
        except_value = ''
        for key, value in except_data.items():
            except_value = value
            key_list = key.split('.')
            for i in key_list:
                try:
                    if i == '*':
                        # 获取*的索引
                        index = key_list.index(i)
                        break
                    else:
                        actual_data = actual_data[i]
                except:
                    raise Exception(
                        f'get data fail , \'{i}\' in keylist={key_list} is not in actual_data={actual_data}')
        actual_result = []
        for di in actual_data:
            flag = True
            for i in range(index + 1, len(key_list)):
                try:
                    di = di[key_list[i]]
                except:
                    log.warning(f'get data fail , \'{key_list[i]}\' in keylist={key_list} is not in actual_data={di}')
                    flag = False
                    break
            else:
                if not flag:
                    continue
                else:
                    actual_result.append(di)
        print(f'actual_result is {actual_result}')
        return actual_result, except_value

    # 校验值存在
    # 字典中多重key且值不确定在哪个key中，规范格式要求data.content.*.order_no 其中*为多重key
    def checkValueIsExist(self, except_data, actual_data):
        actual_result, except_value = self.for_check_value(except_data, actual_data)
        assert except_value in actual_result

    # 同上
    def checkValueNotExist(self, except_data, actual_data):
        actual_result, except_value = self.for_check_value(except_data, actual_data)
        assert except_value not in actual_result


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
    # l = [{"str": "1"}, {"ss": "tst"}]
    # print(l[1])
    # dict1 = {"test1": "1", "test2": "2"}
    # print("test23" in dict1.keys())
