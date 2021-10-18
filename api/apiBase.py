from util.request import RequestsHandler
from conf.sign_key import SpKey
import hashlib
from conf.server_uri_conf import ServerUriConf
import json
from util import util_common
from log.logpro import log
import copy
from lib.common.checker import Checker


class ApiBase(object):
    common_params = {}
    common_body = {}
    common_headers = {}
    common_url = ''
    common_assert = {}
    common_method = ''

    def __init__(self, data, origin_data=None):
        self.data = data
        self.origin_data = origin_data
        self.headers = ''
        self.no_sign_list = []

    def __new__(cls, *args, **kwargs):
        # 模拟final
        if cls != ApiBase and 'process' in cls.__dict__.keys():
            raise Exception('This method cannot be rewritten')
        return super(ApiBase, cls).__new__(cls)

    # data来自case
    # process不可被子类重写
    def process(self):
        self.data_prepare()
        self.do_work()
        self.do_check()
        return self.data

    def data_prepare(self):
        log.info("state exe data_prepare")

        # 将写死的基础数据与使用者自定义的的数据合并
        self.deal_data()

        # 处理上游数据
        # self.data = util_common.get_value_by_rule_in_dict(self.origin_data, self.data)
        if 'params' in self.data:
            self.data['params'] = util_common.get_value_by_rule_in_dict1(self.origin_data, self.data['params'])
        if 'body' in self.data:
            self.data['body'] = util_common.get_value_by_rule_in_dict1(self.origin_data, self.data['body'])


        # 定制化数据 也是准备数据最后一步
        self.customized_data()

    def do_work(self):
        log.info("state exe do_work")
        # TODO 请求主流程
        res = self.do_send()
        if res:
            self.do_format(res)

    # 放在  dataparams 中 用于使用者自定义数据/加密入参、签名(需要根据公司决定)
    def customized_data(self):
        self.signature()
        return

    def do_send(self):
        res = RequestsHandler().method_req(self.data['method'], self.data['url'], self.data['params'],self.data['body'],
                                           self.data['headers'])
        return res

    # 放在  customizedData 中
    def signature(self):
        try:
            key = SpKey.spKeyMap[self.data['params']['sp_no']]
            log.info(f"get sp key {key}")
        except:
            raise KeyError(f"sp_no {self.data['params']['sp_no']} not in spKeyMap")
        # signdata=self.data['params']不行  相当于引用传递 使用同一个内存地址
        # 直接dict.copy 最外层值传递  里层还是引用传递
        sign_data = copy.deepcopy(self.data['params'])
        log.info("-----make sign-----")
        if self.no_sign_list is not None:
            for i in range(len(self.no_sign_list)):
                if self.no_sign_list[i] in sign_data.keys():
                    sign_data.pop(self.no_sign_list[i])
        self.data['params']['sign'] = self.make_sign(key, sign_data)
        log.info(f"sign is {self.data['params']['sign']}")

    def do_check(self):
        check_result = Checker(self.data['assert'], self.data['response']).check()
        if check_result:
            self.data['assert_result'] = True
        # todo 这里应该没用 单条case中如果有校验失败的则上面会抛异常阻断流程
        else:
            self.data['assert_result'] = False

    # TODO 移至工具类
    def make_sign(self, key, arrInput):
        # key=lambda d: d[0]选取元组第一个元素作为比较参数
        # arrInput = sorted(arrInput.items(), key=lambda d: d[0])
        sortedInput = ''
        # 排序元组字段拼接key
        for i in sorted(arrInput):
            ret = self.get_make_sign_string(arrInput[i])
            sortedInput += i + '=' + str(ret) + '&'
        arrInput = sortedInput + 'key=' + key
        log.info("sign with params is {}".format(arrInput))
        # md5
        md5 = hashlib.md5()
        md5.update(arrInput.encode(encoding='utf-8'))
        sign = md5.hexdigest()
        return sign

    # TODO 移至工具类
    # 用于解析多重字典
    def get_make_sign_string(self, arrinput):
        str = ''
        # 判断传入的是字典
        if isinstance(arrinput, dict):
            # 判断字典是空
            if not arrinput:
                print("dict is empty")
                arrinput = ''
                return arrinput
            # 走到这里字典即不空  递归
            for i in sorted(arrinput):
                print("sorted")
                ret = self.get_make_sign_string(arrinput[i])
                # print(ret)
                str += "&" + i + "=" + ret
                # 从第一位开始 即 将第一位的&删除
            arrinput = str[1:]
        else:
            if not arrinput:
                arrinput = ''
                return arrinput
            else:
                return arrinput
        return arrinput

    # TODO 不放到工具类
    def do_format(self, res):
        self.data['response'] = {}
        self.data['response']['headers'] = {}
        if res.content:
            self.data['response'] = json.loads(res.content.decode())
        if res.headers:
            self.data['response']['headers'] = res.headers

    # 处理case数据与接口common数据
    def deal_data(self):
        # todo  copy.deepcopy
        # {**dict1,**dict2} 相当于PHP merge(array1,array2) 即后数组合并前数组 有键重复则以后数组为主
        # self.common_params.copy()

        self.data['params'] = {**self.common_params,
                               **self.data['params']} if 'params' in self.data else self.common_params
        self.data['body'] = {**self.common_body,
                             **self.data['body']} if 'body' in self.data else self.common_body
        self.data['headers'] = {**self.common_headers,
                                **self.data['headers']} if 'headers' in self.data else self.common_headers

        self.data['assert'] = {**self.common_assert,
                               **self.data['assert']} if 'assert' in self.data else self.common_assert
        self.data['method'] = self.common_method
        #修改self.common_url[0]------>self.common_url
        self.data['url'] = ServerUriConf.offlineIP + self.common_url


if __name__ == '__main__':
    # 测试字典update
    # headers = {'a': '111', 'b': '222'}
    # aaaa = {'a': '222', 'c': '222'}
    # headers.update(aaaa)
    # print(headers)
    pass
