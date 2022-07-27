import requests
from log.logpro import log
import json
import urllib.parse
from util.util_aiohttp import AiohttpHandler

indent = '------------------------------------------------------------------------------------------\n'
fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
whistle_proxies = {'http': 'http://127.0.0.1:8899', 'https': 'http://127.0.0.1:8899'}


class RequestsHandler:

    def get_req(self, url, params, headers=None, **kw):
        global response
        try:
            if isinstance(params, dict):
                print(indent + url + '?' + urllib.parse.urlencode(params) + '\n')

            response = requests.get(url, params=params, headers=headers, allow_redirects=True, proxies=whistle_proxies,
                                    verify=False, **kw)
            # response = AiohttpHandler([indent + url + '?' + urllib.parse.urlencode(params) for i in range(5)], 5).eventloop()
            # session = requests.Session()
            # req = session.Request('GET', url, params=params, headers=headers, **kw)
            # prepped = req.prepare()
            # print(indent + 'url is ', prepped.url)
            # # print(indent + 'headers is ', prepped.headers)
            # response = s.send(prepped)e = requests.get(url, params=params, headers=headers, **kw)
        except Exception as e:
            log.fatal(f'get 请求失败 {indent} Exception [{e}]')
            return False
        else:
            log.info(f"{indent} response is \n {response.content.decode()}")
        if response.status_code == 200:
            return response
        else:
            log.fatal(f'response code is [{response.status_code}], response is [{response.content}]')
            return False

    def post_req(self, url, params=None, data=None, headers=None, resBodyFormat=None, **kw):
        try:
            # if isinstance(params, dict) and isinstance(data, dict):
            #     print(url + '?' + urllib.parse.urlencode(params) + '&' + urllib.parse.urlencode(data) + '\n')
            # response = requests.post(url, data=data, params=params, headers=headers, proxies=whistle_proxies,
            #                          verify=False, **kw)
            if resBodyFormat == 'JSON':
                response = requests.post(url, json=data, params=params, headers=headers, proxies=whistle_proxies,
                                         verify=False, **kw)
            else:
                response = requests.post(url, data=data, params=params, headers=headers, proxies=whistle_proxies,
                                         verify=False, **kw)
            # session = requests.Session()
            # req = session.Request('POST', url, params=params, data=data, headers=headers, **kw)
            # prepped = req.prepare()
            # print(indent + 'url is ', prepped.url)
            # print(indent + 'body is ', prepped.body)
            # response = s.send(prepped)
        except Exception as e:
            log.fatal(f'post 请求失败 {indent} Exception [{e}]')
            return False
        else:
            log.info(f"{indent} response is \n {response.content.decode()}")
        if response.status_code == 200:
            return response
        else:
            log.fatal(f'response code is [{response.status_code}], response is [{response.content}]')
            return False

    def method_req(self, method, url, params=None, data=None, headers=None, resBodyFormat=None, **kw):
        log.info(f"request url=={url} ,params=={params} ,data=={data},method=={method} ,headers=={headers} ")
        if method.lower() == 'get' or method == 'get':
            return self.get_req(url, params=params, headers=headers, **kw)
        elif method.lower() == 'post' or method == 'post':
            return self.post_req(url, params=params, data=data, headers=headers, resBodyFormat=resBodyFormat, **kw)
        elif method.lower() == 'put' or method == 'put':
            response = requests.put(url, params=params, data=data, headers=headers,verify=False, **kw)
            log.info(f'{indent} response is \n {response.content.decode()}')
            return response
        else:
            response = requests.request(method, url, **kw)
            log.info(f'{indent} response is \n {response.content.decode()}')
            return response

    # sichuakechuo
    def structure_request(self, url, params=None, data=None, headers=None, **kw):
        params_str = ''
        data_str = ''
        if params:
            for key in params:
                params_str += '&' + key + '=' + params[key]
        # if data:
        #     for key in data:
        #         data_str += '&' + key + '=' + urllib.parse.urlencode(data[key])
        url_str = url + '?' + urllib.parse.urlencode(params_str) + '&' + urllib.parse.urlencode(data)


if __name__ == '__main__':
    # dict1={"a1":{"a11":"123"}}
    import copy

    # url = 'http://ware.m.jd.care/client.action'
    # params = {"functionId": "cartAdd", "testttt": "testtttt"}
    # data = {'area': '184549376_185008128_185008132_0', 'body': 'body', 'build': '3608'}
    # RequestsHandler().structure_request(url=url, params=params, data=data)
    # print({**dict1,**dict2})
    # dict2=copy.deepcopy(dict1)
    # dict2['a1']['a11']="23425"
    # print(dict1)
    # dict1.update(dict2)
    # print(dict1,dict2)

    # response = requests.get(url=url, params=None)
    # print(response.content.decode())
    # params='area=1_72_2799_0&client=android&clientVersion=7.0.0&networkType=wifi&uuid=357177053809351-400E856C137D&body=%7B%27skuId%27%3A+%27782200%27%7D'
    # print(urllib.parse.urlencode(urllib.parse.quote(params)))
