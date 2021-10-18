from api.apiBase import ApiBase


class Client_action(ApiBase):
    common_params = {
        "functionId": "cartAdd",
        "clientVersion": "2.32.0",
        "build": "11335",
        "client": "android",
        "d_brand": "OPPO",
        "d_model": "CPH1607",
        "osVersion": "6.0.1",
        "screen": "1866*1080",
        "partner": "jingdong",
        "androidId": "unknown",
        "installtionId": "36022b5260014b118d9532c64dd88f5a",
        "sdkVersion": "23",
        "uuid": "993bcd78663e6ab3",
        "area": "184549376_185008128_185008132_0",
        "lang": "en_US",
        "country": "MY",
        "eid": "eidA0c4381236bs8ElsZfqmJSjOK+WhF5FcVZhJbGvqqWl7nFGDNKIGRlNsnfdM5EOH4GkpWkNWU4Pwx3ri53vwTNZEmMMgzlkjmqVgqkKHGYdSVXpJY",
        "networkType": "wifi",
        "st": "1634289583564",
        "sign": "556112ed6b3f15cdb68d63c6d8ab3571",
        "sv": "120123123123"
    }
    common_body = {
        "body": "%7B%22businessId%22%3A%22%22%2C%22cartuuid%22%3A%22993bcd78663e6ab3e6148a7d-eb1c-4d02-b6c9-90cdf0bdb985%22%2C%22djrh%22%3A1%2C%22operations%22%3A%5B%7B%22TheSkus%22%3A%5B%7B%22Id%22%3A%2234580436%22%2C%22activePromotionId%22%3A0%2C%22num%22%3A%221%22%2C%22skuPromotionId%22%3A0%7D%5D%2C%22carttype%22%3A%222%22%7D%5D%2C%22syntype%22%3A%221%22%7D",
    }

    common_headers = {
        "host": "api.jd.co.th",
        "cookie": "pin=jdu_FImPjRdURltJ; wskey=AAFhTXmeADDUYyIlimylWU6fgJhEnswhGHLO0dnwU3xXNZe-tvXGJTI3lY7OxFPq1Wv9ugAkYKI",
        "charset": "UTF-8",
        "jdc-backup": "pin=jdu_FImPjRdURltJ; wskey=AAFhTXmeADDUYyIlimylWU6fgJhEnswhGHLO0dnwU3xXNZe-tvXGJTI3lY7OxFPq1Wv9ugAkYKI",
        "accept-encoding": "gzip",
        "cache-control": "no-cache",
        "x-mlaas-at": "wl=0",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "content-length": "351",
        "user-agent": "okhttp/3.12.1",
    }
    common_assert = {
    }
    common_url = '/client.action'
    common_method = 'POST'

    # 准备数据最后一步,支持定制化操作
    def customized_data(self):
        pass
