from api.apiBase import ApiBase
from log.logpro import log
import urllib.parse


class Skudyinfo(ApiBase):
    common_params = {
        "client": "android",
        "uuid": "357177053809351-400E856C137D",
        "clientVersion": "7.0.0",
        "area": "1_72_2799_0",
        "networkType": "wifi",
    }
    common_headers = {
    }
    common_assert = {
        # "ret": "0"
    }
    common_url = '/skuDyInfo',
    common_method = 'get'

    def customized_data(self):
        self.data['params'] = urllib.parse.urlencode(self.data['params'])


if __name__ == '__main__':
    # 测试字典update
    # headers = {'a': '111', 'b': '222'}
    # aaaa = {'a': '222', 'c': '222'}
    # headers.update(aaaa)
    # print(headers)
    # Cashdesk_pc_bankquota.makeSign(Cashdesk_pc_bankquota, "123124", {'sp_no': {'sp_id': '123'}, 'amount': '222'})
    print(1)
