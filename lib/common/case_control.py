import importlib
from log.logpro import log


class Case_control():
    case_req_and_ret_list = {}

    def __init__(self, case_data):
        self.case_data = case_data

    def execute_control(self):
        log.info('case_data: {}'.format(self.case_data))
        for key in self.case_data['stepList']:
            self.case_req_and_ret_list[key] = {}
            scene_class_name = self.case_data['stepList'][str(key)]['scene']
            key = str(key)
            # 执行全部case时 将参数data放入case_req_and_ret_list 格式：case1.0.scene.request/response
            self.case_req_and_ret_list[key][scene_class_name] = {}
            self.case_req_and_ret_list[key][scene_class_name]['request'] = \
                self.case_data['stepList'][str(key)]['params'] if 'params' in self.case_data['stepList'][str(key)] else ''
            log.info('start execute step:{} ,scene:{} process'.format(key, scene_class_name))
            mod = importlib.import_module('api.' + scene_class_name)
            # 实例化process类 TODO 这里可能要改 改为分步骤调用 dataParams,dowork,asserts
            # .capitalize()将字符串第一位字母变成大写 这里有问题 会把除以一个字母外的所有字母变为小写
            data = getattr(mod, scene_class_name.capitalize())(self.case_data['stepList'][str(key)],
                                                             self.case_req_and_ret_list).process()
            self.case_req_and_ret_list[key][scene_class_name] = data

    # arrCheckData = self.doPrepareForCheck()
    # # print(arrCheckData)
    # self.checkCase(arrCheckData)

    # def checkCase(self, arrCheckData):
    #     for case, value in arrCheckData.items():
    #         for step, data in value.items():
    #             for key, ret in data['expectRet'].items():
    #                 if key not in data['actualRet'].keys():
    #                     log.fatal("expect {} not in actual,assert fail".format(key))
    #                     return False
    #                 if data['actualRet'][key] == ret:
    #                     log.info(
    #                         "expect {} equal to actual {} ,assert success".format(ret, data['actualRet'][key]))
    #                     return True
    #
    # # TODO 后续扩展加入校验类型
    # def doPrepareForCheck(self):
    #     arrCheckData = {}
    #     for case, value in self.case_req_and_ret_list.items():
    #         for step, data in value.items():
    #             arrCheckData[case] = {}
    #             arrCheckData[case][step] = {}
    #             arrCheckData[case][step]['expectRet'] = data['assert']
    #             arrCheckData[case][step]['actualRet'] = data['response']
    #     return arrCheckData

# if __name__ == '__main__':
#     # if re.match(r'^case[0-9]?[0-9]{1}$', "case1"):
#     #     print('True')
#     # else:
#     #     print('false')
#     print(''1)
#     test_log().info('filter{}'.format("123"))
