import base64
import json

from api.apiBase import ApiBase
from log.logpro import log
from util.RsaCrypto import RsaCrypto


class api_demo(ApiBase):
    # common 接口常用的不经常更改的数据
    # 与case对应 父类处理数据时会将case的数据相同key的覆盖common数据
    common_params = {
    }
    common_body = {

    }
    common_headers = {
        "Content-Type": "application/json",
    }
    common_assert = {
    }
    common_bodyStr = '''
        {"externalReferenceUid":"jdid_opsmfxcewigg","requestId":"autotest1","event":"autotest1"}
        '''
    common_url = '/account/callback'
    common_method = 'POST'
    common_reqBodyFormat = ''
    api_description = ''
    redis_conf_name = ''
    db_conf_class = ''
    common_host = ''
    # 查询条件
    db_condition = {
        'tableName1': {
            # 查询条件 where
            'conds': {
                'user_pin': '123141'
            },
            # 其他非where条件 list 按元素拼接
            'appends': [
                'order by create_time desc'
            ]
        },
        'tableName2': {
            'conds': {
                'order_id': '1234567',
                'user_pin': 'step.scene.params.data1'
            },
            #
            'appends': [
                'order by create_time desc'
            ]
        }
    }

    # 准备数据最后一步,定制化操作,#父类目前为根据sp_no生成签名，生成签名参数 参数加密都在这里自定义
    def customized_data(self):
        sign_str = base64.b64encode(RsaCrypto('baitiaoPriKey.pem').rsa_sign(self.data['body'], 'SHA-256')).decode()
        self.data['headers']['Authorization'] = sign_str
