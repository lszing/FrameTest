import importlib
from log.logpro import log


class Case_control():
    case_req_and_ret_list = {}

    def __init__(self, case_data):
        log.setLogId(log.generatelogid())
        self.case_data = case_data

    def execute_control(self):
        log.info('case_data: {}'.format(self.case_data))
        for key in self.case_data['stepList']:
            key = int(key)
            self.case_req_and_ret_list[key] = {}
            scene_class_name = self.case_data['stepList'][str(key)]['scene']
            # 执行全部case时 将参数data放入case_req_and_ret_list 格式：case1.0.scene.request/response
            self.case_req_and_ret_list[key][scene_class_name] = {}
            self.case_req_and_ret_list[key][scene_class_name]['params'] = \
                self.case_data['stepList'][str(key)]['params'] if 'params' in self.case_data['stepList'][
                    str(key)] else ''
            self.case_req_and_ret_list[key][scene_class_name]['body'] = \
                self.case_data['stepList'][str(key)]['body'] if 'body' in self.case_data['stepList'][
                    str(key)] else ''
            log.info('start execute step:{} ,scene:{} process'.format(key, scene_class_name))
            mod = importlib.import_module('api.' + scene_class_name)
            # 实例化process类 TODO 这里可能要改 改为分步骤调用 dataParams,dowork,asserts
            # .capitalize()将字符串第一位字母变成大写 这里有问题 会把除以一个字母外的所有字母变为小写
            data = getattr(mod, scene_class_name.capitalize())(self.case_data['stepList'][str(key)],
                                                               self.case_req_and_ret_list).process()
            self.case_req_and_ret_list[key][scene_class_name] = data
        self.case_req_and_ret_list.clear()
if __name__ == '__main__':
    pass
#     # if re.match(r'^case[0-9]?[0-9]{1}$', "case1"):
#     #     print('True')
#     # else:
#     #     print('false')
#     print(''1)
#     test_log().info('filter{}'.format("123"))
