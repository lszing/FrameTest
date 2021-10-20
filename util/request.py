import requests
from log.logpro import log
import json
import urllib.parse


class RequestsHandler:

    def get_req(self, url, params, headers=None, **kw):
        try:
            print(url + '?' + params + '\n')
            response = requests.get(url, params=params, headers=headers, **kw)
        except:
            log.warning("get 请求失败")
            return False
        else:
            log.info(f"response is \n {response.content}")
            return response

    def post_req(self, url, params=None, data=None, headers=None, **kw):
        try:
            print(url + '?' + urllib.parse.urlencode(
                params) + '&' + urllib.parse.urlencode(data) + '\n')
            # print(url+'?'+urllib.parse.urlencode(params))
            response = requests.post(url, data=data, params=params, headers=headers, **kw)
        except:
            log.fatal("post 请求失败")
            return False
        else:
            log.info(f'response is {response.content}')
            if response.status_code == 200:
                return response
            else:
                log.warning(f"POST请求返回状态码为 {response.status_code}  return False")
                return False

    def method_req(self, method, url, params=None, data=None, headers=None, **kw):
        log.info(f"request url=={url} ,params=={params} ,data=={data},method=={method} ,headers=={headers} ")
        if method.lower() == 'get':
            return self.get_req(url, params=params, headers=headers, **kw)
        elif (method.lower() == 'post') or method == 'post':
            return self.post_req(url, params=params, data=data, headers=headers, **kw)
        else:
            return requests.request(method, url, **kw)

    def structure_request(self, url, params=None, data=None, headers=None, **kw):
        params_str = ''
        data_str = ''
        if params:
            for key in params:
                params_str += '&' + key + '=' + params[key]
        # if data:
        #     for key in data:
        #         data_str += '&' + key + '=' + urllib.parse.urlencode(data[key])
        url_str = url + '?' + urllib.parse.urlencode(params_str) +'&'+urllib.parse.urlencode(data)


if __name__ == '__main__':
    # dict1={"a1":{"a11":"123"}}
    import copy

    url = 'http://ware.m.jd.care/client.action'
    params = {"functionId": "cartAdd", "testttt": "testtttt"}
    data = {'area': '184549376_185008128_185008132_0', 'body': 'body', 'build': '3608'}
    RequestsHandler().structure_request(url=url, params=params, data=data)
    # print({**dict1,**dict2})
    # dict2=copy.deepcopy(dict1)
    # dict2['a1']['a11']="23425"
    # print(dict1)
    # dict1.update(dict2)
    # print(dict1,dict2)

    # response = requests.get(url=url, params=None)
    # print(response.content.decode())
