import copy
from log.logpro import log
from util.json_util import ReadJson
from jsonpath import jsonpath


# def get_value_by_rule_in_dict(origin_data, data):
#     # 这里提前定义空字典 防止下面报UnboundLocalError: local variable 'tmp_dict' referenced before assignment
#     tmp_multi_dict = {}
#     if 'params' in data.keys():
#         for key, value in data['params'].items():
#             if not isinstance(key, int) and isinstance(value, str):
#                 key_list = key.split('.')
#                 value_list = value.split('.')
#                 key_count = len(key_list)
#                 value_count = len(value_list)
#                 # key value 长度都大于1才进入  "body.skuId":"1.skuDetail.response.wareInfo.basicInfo.wareId"
#                 # 即多重字典取上游数据
#                 if key_count > 1 and value_count > 1:
#                     # 获取上游数据
#                     # key_value = get_value_by_rule(origin_data, value_list, value_count)
#                     key_value = get_value_by_rule1(origin_data, value)
#                     # 将上游数据加入至key.list中 使用recursion_generate_dict构造字典
#                     key_list.append(key_value)
#                     dict_list = []
#                     dict_list.append(key_list[0])  # 实际最外层key
#                     dict_list.append(recursion_generate_dict(key_list)[key_list[0]])  # 实际最外层key对应的value
#                     # tmp_multi_dict格式 dict={key0:[key,value],key1:[key,value]}
#                     tmp_multi_dict[key] = dict_list  # 多重字典内包列表 key为要删除的
#
#                     # tmp_multi_dict['tmp_key'] = key_list[0]
#                     # tmp_dict = recursion_generate_dict(key_list)[key_list[0]]
#                     # to_delete_key = key
#                     continue
#             # 如果是字典 只能有一种情况 就是 一维字典
#             if isinstance(value, dict):
#                 for k, v in value.items():
#                     # str:{}
#                     if isinstance(v, str) and len(v.split(".")) > 1 and len(key.split(".")) == 1:
#                         # 获取上游数据
#                         k_v = get_value_by_rule1(origin_data, v)
#                         data['params'][key][k] = k_v
#                     # str.str.str:{}
#                     if isinstance(v, str) and len(v.split(".")) > 1 and len(key.split(".")) > 1:
#                         key_list = key.split('.')
#                         k_v = get_value_by_rule1(origin_data, v)
#                         # 将上游数据加入至key_list中 使用recursion_generate_dict构造字典
#                         key_list.append(k)
#                         key_list.append(k_v)
#                         dict_list = []
#                         dict_list.append(key_list[0])  # 实际最外层key
#                         dict_list.append(recursion_generate_dict(key_list)[key_list[0]])
#                         if key not in tmp_multi_dict.keys():
#                             tmp_multi_dict[key] = dict_list
#                         else:
#                             # key已经存在则需要递归合并字典
#                             tmp_multi_dict[key][1] = two_dict_iteration(tmp_multi_dict[key][1], dict_list[1])
#
#             if isinstance(value, str):
#                 str_list = value.split('.')
#                 count = len(str_list)
#                 if count > 1:
#                     key_value = get_value_by_rule1(origin_data, value)
#                     # key_value = get_value_by_rule(origin_data, str_list, count)
#                     # if key_value:
#                     #     data['params'][key] = key_value
#                     data['params'][key] = key_value
#
#     # dict.items遍历方法 不允许在遍历过程中修改字典格式 因此上面遍历完 加入字典 格式为{要删除key:[实际key:实际value]}
#     if tmp_multi_dict:
#         for key, value in tmp_multi_dict.items():
#             if value[0] not in data['params'].keys():
#                 data['params'][value[0]] = value[1]
#             else:
#                 data['params'][value[0]].update(value[1])
#             del (data['params'][key])
#     # if tmp_multi_dict:
#     #     data['params'][tmp_key] = tmp_dict
#     #     del (data['params'][to_delete_key])
#     return data


# 目前使用这个 10.18删除 "if 'params' in data.keys():" 且将data['params']改为data apiBase中调用两次
def get_value_by_rule_in_dict1(origin_data, data):
    # 这里提前定义空字典 防止下面报UnboundLocalError: local variable 'tmp_dict' referenced before assignment
    tmp_multi_dict = {}
    for key, value in data.items():
        if not isinstance(key, int) and isinstance(value, str):
            key_list = key.split('.')
            key_count = len(key_list)
            # key value 长度都大于1才进入  "body.skuId":"1.skuDetail.response.wareInfo.basicInfo.wareId"
            # 即多重字典取上游数据
            if key_count > 1:
                # 获取上游数据
                key_value = get_value_by_rule1(origin_data, value)
                # key_value = get_value_by_rule2(origin_data, value)
                # 将上游数据加入至key.list中 使用recursion_generate_dict构造字典
                key_list.append(key_value)
                dict_list = []
                dict_list.append(key_list[0])  # 实际最外层key
                dict_list.append(recursion_generate_dict(key_list)[key_list[0]])  # 实际最外层key对应的value
                # tmp_multi_dict格式 dict={key0:[key,value],key1:[key,value]}
                tmp_multi_dict[key] = dict_list  # 多重字典内包列表 key为要删除的

                # tmp_multi_dict['tmp_key'] = key_list[0]
                # tmp_dict = recursion_generate_dict(key_list)[key_list[0]]
                # to_delete_key = key
                continue
        # 如果是字典 只能有一种情况 就是 一维字典
        if isinstance(value, dict):
            for k, v in value.items():
                # str:{}
                if isinstance(v, str) and len(v.split(".")) > 1 and len(key.split(".")) == 1:
                    # 获取上游数据
                    k_v = get_value_by_rule1(origin_data, v)
                    data[key][k] = k_v
                # str.str.str:{}
                if isinstance(v, str) and len(v.split(".")) > 1 and len(key.split(".")) > 1:
                    key_list = key.split('.')
                    k_v = get_value_by_rule1(origin_data, v)
                    # 将上游数据加入至key_list中 使用recursion_generate_dict构造字典
                    key_list.append(k)
                    key_list.append(k_v)
                    dict_list = []
                    dict_list.append(key_list[0])  # 实际最外层key
                    dict_list.append(recursion_generate_dict(key_list)[key_list[0]])
                    if key not in tmp_multi_dict.keys():
                        tmp_multi_dict[key] = dict_list
                    else:
                        # key已经存在则需要递归合并字典
                        tmp_multi_dict[key][1] = two_dict_iteration(tmp_multi_dict[key][1], dict_list[1])

        if isinstance(value, str):
            str_list = value.split('.')
            count = len(str_list)
            if count > 1:
                key_value = get_value_by_rule1(origin_data, value)
                # key_value = get_value_by_rule(origin_data, str_list, count)
                # if key_value:
                #     data['params'][key] = key_value
                data[key] = key_value

    # dict.items遍历方法 不允许在遍历过程中修改字典格式 因此上面遍历完 加入字典 格式为{要删除key:[实际key:实际value]}
    if tmp_multi_dict:
        for key, value in tmp_multi_dict.items():
            if value[0] not in data.keys():
                data[value[0]] = value[1]
            else:
                data[value[0]].update(value[1])
            del (data[key])
    # if tmp_multi_dict:
    #     data['params'][tmp_key] = tmp_dict
    #     del (data['params'][to_delete_key])
    return data


# 递归处理多重key 构造多重字典  [1,2,3,4,5,6,7,8] ====>{1:{2:{3:{4:{5:{6:{7:8}}}}}}}}
def recursion_generate_dict(key_list, i=0, _dict=None):
    if _dict is None:
        _dict = {}
    if i == len(key_list) - 2:
        _dict[key_list[i]] = key_list[i + 1]
    if i < len(key_list) - 2:
        _dict[key_list[i]] = recursion_generate_dict(key_list, i + 1)
    return _dict


# 递归处理字典
def recursion_dict(origin_data):
    for key, value in origin_data.items():
        if isinstance(value, dict):
            return recursion_dict(value)
        else:
            return value


# 通过规则获取上游数据
# def get_value_by_rule(origin_data, key_list, count):
#     temp_ret = copy.deepcopy(origin_data)
#     for j in range(count):
#         try:
#             # tempRet.get(keyList[j])
#             temp_ret = temp_ret[key_list[j]]
#             count -= 1
#         except:
#             # 进入这里则认为没有,跳过本次循环
#             continue
#     # 只有count==0时才是获取到了数据
#     if count == 0:
#         return temp_ret
#     return False


# def get_value_by_rule2(origin_data, str):
#     try:
#         str = jsonpath(origin_data, str)
#     except:
#         log.warning(f"str={str} not obtained from origin_data={origin_data}")
#     return str


# 通过规则获取上游数据
def get_value_by_rule1(origin_data, str) -> str:
    temp_ret = copy.deepcopy(origin_data)  # dict1=dict2.copy()
    str_list = str.split(".")
    count = len(str_list)
    for j in range(count):
        try:
            # tempRet.get(keyList[j])
            if str_list[j].isdigit():
                str_list[j] = int(str_list[j])
            temp_ret = temp_ret[str_list[j]]
            count -= 1
        except:
            # 进入这里则认为没有,跳过本次循环
            continue
    # 只有count==0时才是获取到了数据
    if count == 0:
        return temp_ret
    # 未获取到数据返回原字符串
    log.warning(f"str={str} not obtained from origin_data={origin_data}")
    return str


def get_value_by_rule2(origin_data, s) -> str:
    if isinstance(s, str) and len(s.split('.')) > 1:
        temp_ret = copy.deepcopy(origin_data)  # dict1=dict2.copy()
        str_list = s.split(".")
        count = len(str_list)
        for j in range(count):
            try:
                if str_list[j].isdigit():
                    str_list[j] = int(str_list[j])
                temp_ret = temp_ret[str_list[j]]
                count -= 1
            except:
                # 进入这里则认为没有,跳过本次循环
                continue
        # 只有count==0时才是获取到了数据
        if count == 0:
            return temp_ret
        # 未获取到数据返回原字符串
        log.warning(f"str={str} not obtained from origin_data={origin_data}")
    return s


# 递归合并多维字典
# dict1 {'skuId': {'test1': {'test2': '782200'}}}
# dict2 {'skuId': {'test1': {'test3': '782200'}}}
# 结果 {'skuId': {'test1': {test2': '782200','test3': '782200'}}}
def two_dict_iteration(dict1, dict2):
    # 直接遍历.keys()无法在遍历时修改字典大小 加入列表遍历可以
    for k1, k2 in list(zip(dict1.keys(), dict2.keys())):
        if k1 == k2:
            result_dict = two_dict_iteration(dict1[k1], dict2[k2])
            dict1[k1] = result_dict
        else:
            dict1[k2] = dict2[k2]
    return dict1


# self.result_dict = {}
# self.result_dict['except_data'] = {}
# self.result_dict['actual_data'] = {}
update_result_list = []


class util_common:
    def __init__(self):
        self.result_dict = {}
        self.result_dict['except_data'] = {}
        self.result_dict['actual_data'] = {}

    # 递归获取case层定义的多重字典或”content.data.sp_no“
    def recursive(self, except_data, actual_data):
        # 这里要 兼容 "<withkeys>": "code"
        if isinstance(except_data, str):
            self.result_dict['except_data'][0] = except_data
            self.result_dict['actual_data'][0] = actual_data
            return self.result_dict
        # 这里要 兼容 "<withkeys>": ["code","content"]
        if isinstance(except_data, list):
            for i in range(len(except_data)):
                try:
                    self.result_dict['actual_data'] = actual_data
                    self.result_dict['except_data'][i] = except_data[i]
                except:
                    raise AssertionError(
                        f'get data fail ,{except_data[i]} is not in actual_data={actual_data}')
            return self.result_dict
        key_list = except_data.keys()
        value_list = except_data.values()
        # 判断字典中有多个key 则分别处理
        # if len(key_list) > 1:
        for key in key_list:
            # 分别判断每一个key 若是a.b.c="***"则直接取值
            split_list = key.split('.')

            if len(split_list) > 1:
                split_actual_data = copy.deepcopy(actual_data)
                try:
                    for i in split_list:
                        # 这里根据切分完的循环获取值
                        split_actual_data = split_actual_data[int(i) if i.isdigit() else i]
                    self.result_dict['except_data'][split_list[len(split_list) - 1]] = except_data[key]
                    self.result_dict['actual_data'][split_list[len(split_list) - 1]] = split_actual_data
                except:
                    raise AssertionError(
                        f'get data fail , \'{i}\' in keylist={split_list} is not in actual_data={split_actual_data}')
            # 若不是a.b.c="***" 而是a="b" 直接将数据放入结果中
            elif (not isinstance(except_data[key], dict)):
                try:
                    self.result_dict['actual_data'][key] = actual_data[key]
                    self.result_dict['except_data'][key] = except_data[key]
                except:
                    log.warning(
                        f'get data fail ,key \' {key} \' is not in actual_data={actual_data},this  key return None ')
                    raise AssertionError(f'get data fail ,\'{key}\'  is not in actual_data={actual_data}')
            # 进入这里则是多重字典
            else:
                mult_actual_data = copy.deepcopy(actual_data)
                mult_except_data = copy.deepcopy(except_data)
                try:
                    mult_actual_data = mult_actual_data[int(key) if key.isdigit() else key]
                    mult_except_data = mult_except_data[key]
                except:
                    raise AssertionError(f'get data fail ,\'{key}\'  is not in actual_data={actual_data}')
                # todo  10.12 修改 兼容 haskey"<withkeys>": {
                #   "data": {
                #     "content": ["sp_no","amount"]
                #   },
                #   "data1": ["amount","sp_no"]
                # }
                # 如使用其他校验方法有问题 检查这里 之前是 前面有return
                self.recursive(mult_except_data, mult_actual_data)
        return self.result_dict


if __name__ == '__main__':
    # data = ReadJson('test1').readJson()
    #
    # except_data = data[0]['except_data']['response']['<notequal>']
    # actual_data = data[1]['actual_data']['response']
    # print(recursive(except_data, actual_data))
    # dict1 = {"a": {"b": {"c": "d"}}}
    # print(recursion_dict(dict1))
    # list1 = ["a", "b", "c", "d"]
    # print(recursion_generate_dict(list1))
    # userdict = {}
    # userdict[('site1', 'board1', 'username')] = 'tommy'
    # print(userdict)
    # dict1 = {'skuId3': {'test1': {'test2': '782200'}}}
    # dict2 = {'skuId3': {'test1': {'test3': '782200'}}}
    # print(two_dict_iteration(dict1, dict2))
    json = {1: {
        'loginSubmit': {'scene': 'loginSubmit', 'params': {'params': 'eyJ'}, 'assert': {'response': {'code': 1}},
                        'body': {}, 'headers': {}, 'method': 'GET', 'resBodyFormat': None,
                        'url': 'http://account-api.joybuy.com/user1/loginSubmit',
                        'response': {'code': 1, 'message': 'success',
                                     'result': {'mfs_session': '75AB88DFFDD641AAC6905EA73415DF0E',
                                                'pin': 'cbb2b_0X1SQxi99qVoQzD1HE',
                                                'mfs_pin': 'ceeff31cf2b70d80a983dad51fd6870b063359282bda9d6a4f232c22e25a2d9d',
                                                'upgradeType': 0, 'returnUrl': 'http://www.joybuy.com'},
                                     'success': True,
                                     'headers': {'Server': 'openresty', 'Date': 'Wed, 27 Jul 2022 02:37:40 GMT',
                                                 'Content-Type': 'text/plain;charset=UTF-8',
                                                 'Transfer-Encoding': 'chunked', 'Connection': 'close',
                                                 'Vary': 'Accept-Encoding', 'Access-Control-Allow-Credentials': 'true',
                                                 'Access-Control-Allow-Methods': 'GET, HEAD, POST, OPTIONS',
                                                 'Access-Control-Allow-Headers': 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Access-Control-Allow-Origin,Authorization',
                                                 'Access-Control-Max-Age': '3600',
                                                 'Set-Cookie': 'mfs_session=75AB88DFFDD641AAC6905EA73415DF0E; Max-Age=345600; Expires=Sun, 31-Jul-2022 02:37:40 GMT; Domain=joybuy.com; Path=/, mfs_pin=ceeff31cf2b70d80a983dad51fd6870b063359282bda9d6a4f232c22e25a2d9d; Max-Age=345600; Expires=Sun, 31-Jul-2022 02:37:40 GMT; Domain=joybuy.com; Path=/',
                                                 'Expires': 'Wed, 27 Jul 2022 02:37:40 GMT',
                                                 'Cache-Control': 'max-age=0', 'Content-Encoding': 'gzip'}},
                        'assert_result': True}}, 2: {'loginSubmit': {
        'params': {'loginName': 'prelushuzhi8@jd.com', 'pwd': 'm1234567',
                   'withoutPlatformCode': '$1.loginSubmit.params.params'}, 'body': ''}}}
    a = '$...params'
    print(jsonpath(json, a))
