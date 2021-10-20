from api.apiBase import ApiBase 


class Client_action(ApiBase): 
    common_params = {
        "functionId": "cartAdd",
    }
    common_body = {
        "area": "184549376_185008128_185008132_0",
        "body": "{\"noResponse\":false,\"djrh\":\"1\",\"cartuuid\":\"hjudwgohxzVu96krv\/T6Hg==\",\"carttype\":\"2\",\"syntype\":\"1\",\"openudid\":\"5ef7b42d6858afa48fce24fddc16a16b909d493d\",\"operations\":[{\"theSkus\":[{\"id\":\"57519096\",\"num\":\"1\",\"storeId\":\"\",\"skuUuid\":\"\",\"deliveryId\":\"\",\"activePromotionId\":0}],\"carttype\":\"2\"}]}",
        "build": "3608",
        "client": "apple",
        "clientVersion": "2.33.0",
        "country": "TH",
        "d_brand": "apple",
        "d_model": "iPhone13,4",
        "eid": "eidIdce781214esaxRm2boYERkOOA04TXptFx8UZt+hlZaY4t8YqxT2JZNhnL5AxPd7wknFh+n/612o2pUvBiHKU2/YAELYu614Y8CMj7b+M3kEuovhL",
        "isBackground": "N",
        "lang": "en_US",
        "networkType": "wifi",
        "networklibtype": "JDNetworkBaseAF",
        "openudid": "5ef7b42d6858afa48fce24fddc16a16b909d493d",
        "osVersion": "15.0",
        "partner": "appstore",
        "scope": "01",
        "screen": "1284*2778",
        "sign": "18fb9e718c7d5ef18f4bfc6fb2d5f7d1",
        "st": "1634699963067",
        "sv": "110",
        "uuid": "hjudwgohxzVu96krv/T6Hg==",
        "wifiBssid": "unknown",
    }
    common_headers = {
        "host": "api.jd.co.th",
        "cookie": "pin=jdu_wOaQPPutLxwj;wskey=AAFhbOFyADBLYm5cjoT6BewKuExoD6cUCLrbFSROP6vLmvkJmdztyJk7ZLejO9a7vgx8BcPvjHI;whwswswws=;jmp=5d65e6792d870aa82b846a97da4a230e0ccd36de305452e629d0d3a0fb28026b;criteo=f5595a3b840386e57844d247bd5d4a5190ffa04016ed56b953c4bfb3d2ed7b3b",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "accept-encoding": "gzip",
        "user-agent": "THAppModule_Example/2.33.0 (iPhone; iOS 15.0; Scale/3.00)",
        "accept-language": "zh-Hans-CN;q=1",
        "content-length": "1031",
    }
    common_assert = {
    }
    common_url = '/client.action'
    common_method = 'POST'

    #准备数据最后一步,支持定制化操作,#父类目前为根据sp_no生成签名
    def customized_data(self):
        pass 
