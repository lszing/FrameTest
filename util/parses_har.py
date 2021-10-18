import os
import json
import re


class ParsesHar():
    def __init__(self, file_name):
        self.file_name = file_name
        self.path = ''

    def parses(self):
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
                    indent * 2 + '\"' + index['name'] + '\": ' + '\"' + re.sub('\"', '\\\"', re.sub('\'', '\\\'', index[
                        'value'])) + '\",\n')

            # value['name'] + '\": ' + '\"' + index['value'].replace('\"','\\\"').replace('\'', '\\\'') if isinstance(index['value'], str) else index['value']
            if 'postData' in request_data.keys():
                for index in request_data['postData']['params']:
                    w.write(indent * 2 + '\"' + index['name'] + '\": ' + '\"' + re.sub('\"', '\\\"',
                                                                                       re.sub('\'', '\\\'', index[
                                                                                           'value'])) + '\",\n')
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
            url = request_data['url'].split('?')[0].split('/').pop()
            w.write(indent + 'common_url = \'/' + url + '\'\n')

            # common_method
            w.write(indent + 'common_method = \'' + request_data['method'] + '\'\n\n')

            # customized_data
            w.write(indent + '#准备数据最后一步,支持定制化操作 \n')
            w.write(indent + '# def customized_data(self):\n')
            w.write(indent + '#' + indent * 2 + 'pass \n')


if __name__ == "__main__":
    ParsesHar("client.action").parses()
    strrr = "120"
    # isinstance(st1r, str): st1r?"123"
    print(re.sub('\"', '\\\"', re.sub('\'', '\\\'', strrr)))
