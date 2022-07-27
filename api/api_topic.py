from api.apiBase import ApiBase
from conf.server_uri_conf import ServerUriConf


class Api_topic(ApiBase):
    common_params = {
    }
    common_body = {
        "mid": 14,
        "email": "email3",
        "title": "testt",
    }
    common_headers = {
    }
    common_assert = {
    }
    common_url = '/api/topic/'
    common_method = 'POST'
    common_resBodyFormat = 'JSON'

    db_conf = 'test_db'
    db_conds = {
        'conds': '',
        'options': '',
        'appends': ''
    }

    # 准备数据最后一步,支持定制化操作,#父类目前为根据sp_no生成签名
    def customized_data(self):
        self.data['url'] = ServerUriConf.localIP + self.common_url
        # if 'test_flag' in self.data['body'] and self.data['body']['test_flag']=='1':

    # def do_format(self, res):
    #     self.data['response'] = {}
    #     if res.content:
    #         self.data['response'] = eval(res.content.decode('utf-8'))
