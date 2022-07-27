import os
import json
import re
from urllib import parse
import json


class ParsesHar():
    def __init__(self, file_name):
        self.file_name = file_name
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def parses(self):
        file = self.path + '/' + 'resources' + '/' + self.file_name + '.har'
        with open(file, 'r', encoding="UTF-8") as f:
            har_data = json.load(f)
        request_dict = har_data['log']['entries'][0]['request']
        response_dict = har_data['log']['entries'][0]['response']
        print(request_dict)
        self.har_to_api(request_dict)

    def har_to_api(self, request_data):
        if len(self.file_name.split('.')) > 1:
            self.file_name = re.sub('\\.', '_', self.file_name)
        if len(self.file_name.split('/')) > 1:
            self.file_name = re.sub('/', '_', self.file_name)

        write_file = self.path + '\\api\\' + self.file_name + '.py'
        print(write_file)
        with open(write_file, "w+", encoding='UTF-8') as w:
            w.write('from api.apiBase import ApiBase \n\n\n')

            w.write('class ' + self.file_name.capitalize() + '(ApiBase): \n')
            indent = '    '

            # common_params
            w.write(indent + 'common_params = {\n')
            for index in request_data['queryString']:
                w.write(
                    indent * 2 + '\"' + index['name'] + '\": ' + '\"' + re.sub('\"', '\\\"',
                                                                               re.sub('\'', '\\\'', parse.unquote(index[
                                                                                                                      'value']))) + '\",\n')
            w.write(indent + '}\n')

            # common_body
            w.write(indent + 'common_body = {\n')
            # value['name'] + '\": ' + '\"' + index['value'].replace('\"','\\\"').replace('\'', '\\\'') if isinstance(index['value'], str) else index['value']
            if 'postData' in request_data.keys():
                if request_data['postData']['mimeType'] == 'application/json':
                    self.resBodyFormat = 'JSON'
                    request_json_data = json.loads(request_data['postData']['text'])
                    for key, value in request_json_data.items():
                        # parse.unquote===urldecode
                        w.write(indent * 2 + '\"' + key + '\": ' + '\"' + str(value) + '\",\n')
                if request_data['postData']['mimeType'] == 'application/x-www-form-urlencoded':
                    for index in request_data['postData']['params']:
                        w.write(indent * 2 + '\"' + index['name'] + '\": ' + '\"' + re.sub('\"', '\\\"',
                                                                                           re.sub('\'', '\\\'',
                                                                                                  parse.unquote(index[
                                                                                                                    'value']))) + '\",\n')
                # todo
                # for index in request_data['postData']['text']:
                #     w.write(indent * 2 + '\"' + index['name'] + '\": ' + '\"' + re.sub('\"', '\\\"',
                #                                                                        re.sub('\'', '\\\'',
                #                                                                               parse.unquote(index[
                #                                                                                                 'value']))) + '\",\n')
            w.write(indent + '}\n')

            # common_headers
            w.write(indent + 'common_headers = {\n')
            for index in request_data['headers']:
                w.write(
                    indent * 2 + '\"' + index['name'] + '\": ' + '\"' + re.sub('\"', '\\\"', re.sub('\'', '\\\'', index[
                        'value'])) + '\",\n')
            w.write(indent + '}\n')

            # common_assert
            w.write(indent + 'common_assert = {\n')
            # todo assert
            w.write(indent + '}\n')
            request_data['url'].split('/')

            # common_url
            # url = request_data['url'].split('?')[0].split('/').pop()
            url_list = request_data['url'].split('?')[0].split('/')
            url_list.pop(0)
            url_list.pop(0)
            url_list.pop(0)
            url = '/'.join(url_list)
            w.write(indent + 'common_url = \'/' + url + '\'\n')

            # common_method
            w.write(indent + 'common_method = \'' + request_data['method'] + '\'\n\n')

            # common_resBodyFormat post请求数据是否为json
            if self.resBodyFormat:
                w.write(indent + 'common_resBodyFormat = \'' + self.resBodyFormat + '\'\n\n')

            # customized_data
            w.write(indent + '#准备数据最后一步,支持定制化操作,#父类目前为根据sp_no生成签名\n')
            # w.write(indent + '# def customized_data(self):\n')
            # w.write(indent + '#' + indent * 2 + 'pass \n')
            w.write(indent + 'def customized_data(self):\n')
            w.write(indent * 2 + 'pass \n')

    def har_to_data(self):
        data_file = self.path + '/' + 'data' + '/' + 'test_' + self.file_name + '.json'
        print(data_file)
        with open(data_file, 'w+', encoding='UTF-8') as w:
            indent = '  '
            w.write('{ \n')
            w.write(indent + '\"case1\": {\n')
            w.write(indent * 2 + '\"info\":\"\",\n')
            w.write(indent * 2 + '\"stepList\": {\n')
            w.write(indent * 3 + '\"1\": {\n')
            w.write(indent * 4 + '\"scene\": \"' + self.file_name + '\",\n')
            w.write(indent * 4 + '\"assert\": {\n')
            w.write(indent * 5 + '\"response\": {\n')
            w.write(indent * 6 + '\"code\": 0\n')
            w.write(indent * 5 + '}\n')
            w.write(indent * 4 + '}\n')
            w.write(indent * 3 + '}\n')
            w.write(indent * 2 + '}\n')
            w.write(indent + '}\n')
            w.write('}\n')


if __name__ == "__main__":
    par = ParsesHar("getransformlinks111")
    par.parses()
    par.har_to_data()
    # print('pytest -v -s --path test_gettransformlinks Suites/test_api.py')
    # strrr = "120"
    # isinstance(st1r, str): st1r?"123"
    # print(re.sub('\"', '\\\"', re.sub('\'', '\\\'', strrr)))
