from api.apiBase import ApiBase
from log.logpro import log


class Cashdesk_pc_bankquota(ApiBase):
    common_params = {
        "sp_no": "1000023439",
        "source_flag": "0",
        "version": 10,
        "ua": "BaiduWallet-6.1.0.0-IOS-_720_1200_iPhone_10.3.2_10.3.2_baidu"
    }
    common_headers = {
        "fddf": "123"
    }
    common_assert = {
        # "ret": "0"
    }
    common_url = '/bankquota'
    common_method = 'get'

    def customized_data(self):
        if 'otherParams' in self.data.keys() and self.data['otherParams'] is not None:
            self.no_sign_list.append(self.data['otherParams']['mistakeSign'])
        super(Cashdesk_pc_bankquota, self).customized_data()


if __name__ == '__main__':
    # 测试字典update
    # headers = {'a': '111', 'b': '222'}
    # aaaa = {'a': '222', 'c': '222'}
    # headers.update(aaaa)
    # print(headers)
    # Cashdesk_pc_bankquota.makeSign(Cashdesk_pc_bankquota, "123124", {'sp_no': {'sp_id': '123'}, 'amount': '222'})
    print(1)
