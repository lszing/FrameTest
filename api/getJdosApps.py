from api.apiBase import ApiBase


class Getjdosapps(ApiBase):
    common_params = {

    }

    common_headers = {
        "Host": "forcebot-api.jd.com",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Origin": "http://forcebot.jd.com",
        "Referer": "http://forcebot.jd.com/",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "__jdv=247986820|direct|-|none|-|1634033349220; __jdu=16340333492191629788394; jd.erp.lang=zh_CN; jdd69fo72b8lfeoe=ZB5FLWS355YQYOIE4UQIPRO7IJ7THZFMJ3II2XQQZF23DY6UAOKVUZY7LN6V2EIPUIDNF5NUQUULQB5J6HOAX5VLHQ; jdc_art=1634033399560-t28SlKLrj-IzYJuqfld6KEmt3T5o4hoj; jdc_art.sig=4WUXLmih2aMWROK3yguqQ6dQZl4; mba_muid=16340333492191629788394; erp1.jd.com=B8AA9F93987A09747B5E220EDDEA6D18E2AB2C6D866BAAC0920204EE8DFFAACB17D4A09376F4596237FA3F11B50990F0062F6BBBB17B7438568D3A71020298C2982D9CEF61B32B2D49E7F5AEB88C36CE; sso.jd.com=BJ.71DA126C5ECC65235B33600E0D2537D54120211014134435; RT=\"z=1&dm=jd.com&si=xujbmydxev9&ss=kuqnybtw&sl=1&tt=uq&ld=2g4\"; __jdc=256005660; __jda=256005660.16340333492191629788394.1634033349.1634205282.1634213332.8; __jdb=256005660.5.16340333492191629788394|8.1634213332",
        "Connection": "keep-alive",
    }
    common_assert = {
    }
    common_url = '/http://forcebot-api.jd.com/api/testcase/getJdosApps'
    common_method = 'GET'
