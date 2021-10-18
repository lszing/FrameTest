from api.apiBase import ApiBase
from log.logpro import log
import urllib.parse


class Skudetail(ApiBase):
    common_params = {
        "area": "1_72_2799_0",
        "client": "android",
        "clientVersion": "7.0.0",
        "networkType": "wifi",
        "uuid": "357177053809351-400E856C137D",
        'body': {
            'skuId': "782200"
        }
    }
    common_headers = {
    }
    common_assert = {
        # "ret": "0"
    }
    common_url = '/skuDetail'
    common_method = 'get'
    #入参数组格式需要urlencode
    def customized_data(self):
        self.data['params'] = urllib.parse.urlencode(self.data['params'])


if __name__ == '__main__':
    # Cashdesk_pc_bankquota.makeSign(Cashdesk_pc_bankquota, "123124", {'sp_no': {'sp_id': '123'}, 'amount': '222'})
    pass