import rsa
import os
import base64
import hashlib
from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
import re

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
save_path = path + '/lib/rsaKey/'

with open(file=save_path + 'pubKey.pem', mode='r') as f:
    pubK = f.read()
    public_key = rsa.PublicKey.load_pkcs1(pubK.encode())
with open(file=save_path + 'priKey.pem', mode='r') as f:
    priK = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(priK.encode())


class RsaCrypto:

    def generate_ras_key(self):
        (pubKey, prikey) = rsa.newkeys(1024)
        with open(file=save_path + 'pubKey.pem', mode='w+') as f:
            f.write(pubKey.save_pkcs1().decode())
        with open(file=save_path + 'priKey.pem', mode='w+') as f:
            f.write(prikey.save_pkcs1().decode())

    @classmethod
    def public_encrypt(cls, data: str) -> bytes:
        crypt_data = rsa.encrypt(data.encode('utf-8'), public_key)
        return crypt_data

    @classmethod
    def public_decrypt(cls, data: bytes) -> str:
        decrypt_data = rsa.decrypt(data, private_key).decode('utf-8')
        return decrypt_data

    '''
    hash_name:
        'MD5', 'SHA-1','SHA-224', SHA-256', 'SHA-384' or 'SHA-512'
    '''

    @classmethod
    def rsa_sign(cls, signstr: str, hash_method: str) -> bytes:
        crypt_sign = rsa.sign(signstr.encode('utf-8'), private_key, hash_method)
        return crypt_sign

    @classmethod
    def rsa_verify(cls, data: str, signedData: bytes) -> str:
        hash_name = rsa.verify(data.encode('utf-8'), signedData, public_key)
        return hash_name


# ttttt = RsaCrypto.public_encrypt("tststs")
# print(RsaCrypto.public_decrypt(ttttt))
# wwww = RsaCrypto.rsa_sign('test', 'SHA-1')
# print(wwww)
# print(RsaCrypto.rsa_verify('test', wwww))

BLOCK_SIZE = AES.block_size
# 补位
pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * '='
# 去除补位
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESTest:
    CIPHER_PARAM = 'AES/CBC/PKCS5Padding'

    jd = 'jdfans'
    md5 = hashlib.md5()
    md5.update(jd.encode())
    jdfansMd5 = md5.hexdigest().upper()

    # key
    jdfan16 = jdfansMd5[0:16].encode()

    # 偏移量
    jdfan32 = jdfansMd5[16:].encode()

    def tt(self, s: str):
        print(self.jdfan16)
        print(self.jdfan32)
        cipher = AES.new(self.jdfan16, AES.MODE_CBC, self.jdfan32)
        # s = pad(s)
        decoder = base64.b64decode(s)
        # s = s.replace('-', '+')
        # s = s.replace('_', '/')
        decoder = pad(decoder)
        print(decoder)
        decryped_text = cipher.decrypt(decoder)
        print(decryped_text)
        decryped_text = decryped_text.decode('utf-8', errors='ignore')
        # result = unpad(decryped_text)
        return decryped_text


b = 'yqSFaf_WL1_4iRlinm64GDoMBFH9EE8rxWE0cXAhsbNH-9Sy6t3EYYMlBM7Ws6vAdYztYPEEtBvt0A-lvVYUxAXBE5mXSGOxpN2gsDWmsJSu8y-c1lVa-gWfJc2N4Gllx-JAU5hTJZPypcLFUl6yHpJ1j5k2178SddBifh8DdtLkf0FoTEtgkMIaE_d3H6sMeShNJ59dzR0FIIy0lMFKwnrY9Qzfqd4iiUk02n8ik28XWD7fA2XC3JzF9Ws8nkQpeqidHjWSzg6N2oAL7Ko9Fd0tsQPX-RUCqI-O8-DrqhSkNq5Ygnu1AT7r_SvFDvPROtoHHe27MfmCgtN_1RUssVlhlJ_BN-abIJa8p18tcjuzX95GAHWla2S4Nx6k8yWJ5L9dEzcG0qcSyowFRU2lbRXXIqjwSpN440QI91Q3izQnRk0x_qF2ZrPLOKmde53odM8oDFhm8FAFDVwRpiVvhYZ5wLpekm8_uG1n5XLmjcatkgT9C9_7l16vSnxRLT34b78OVZtIq6ymopeXSwGw9XJgGF6jp2UBRdUmNJnmOEty-ZIkQyY_OrscsUuN38v-6eyPDK0l1lFZrveCI161_mzGhokmFnDMiTeCo6JUl-YfjG0M69rQrnL0UyIzsxjmzV9pYtSjHE7p1lc8uki7V9mM_QHow9vFI9zSw8IgiYUzfyYyOmJ6tvNpmekMPIF0SrqMbyNUqqHAoYJmVY49TVt0NhjZWg-QBC_-cYAxSRWjfdnD--5UM7pJ4_3Ty-SHvO4-R7f9pAbX_K2uBeNcBGWwEHseJWyaQklpvq6ZnsixaceamuJ5tNyPt79F9h2g0wf_pi9bc5lOteBFhGtdpEz5fs_39owjn9Lv6nqriWiv1OI__YbHWmdhxkPg2rPNZFl-ZjLNkhH4zTNvJ3MzWAom8jcNzKfT6yoA_jyCF446hCN-YM2lZqTsxBm0BNST-FmWi64bGqoxWAjADfRo28rVlW7WYQfnFbyk0L8dtAWX7IEa1fbMhpqC6z4aNzzhOGFLFYIUQ1XJQfOcXMYS8_ZmR2-1JSp_Qza3VviLfOqNrbKl5psiXH37LGXMcgTe-OGNhXYbQuuLBfqwdMSntb-_0XJImsVScDtmXu2oT65ZpPR9FiV4QvS7NPMcjGVK_93exLA3LdcS3jEdnI_MEQA4VNChPMdi6oq78menegExIL5jUWblkJeUISDKBGKykmBrD8TS2_9PSo37RyMqDiPZYzekE2WmXukzaJ129UH21inMS-WFrQ70qtWcYHUR_D1Ugnm-VFm-ftBnl8DJvKHkSxECWWl5YbwnerPEbbX7IvoHtjVCEfE3MIvv2I3XShJSYyTHarhP6TG_6IK6dMKHArYpPYZVzTaw4VKqC6JcxBAjIvXlLhIEysM2a9sA4mR9j1iSgmJ8rXjEzi9V_-9zVF9l7MVBRIqy2exBjlJVJKP_56Hx9ApOGxoPpOstpyQj_7p2VngxpCVIjZRo0DklloTr7syNc2PzHiEhVIVR25YwDnYBDSO6M_2BdTVEzU-t03TkBMWjxhvrHKFmpWM6FgO7F1R-TsBY8HQ0H03mYJWZxOQtugPVDRx1YwkfcKUCJicv3XXqW5TUP2dzHg'
a = 'rOpDrh85sk0I_AnwxsF9P1ogod3MMgXKbuQMS_MC4X3LYs6p9ye6fF-elt_2i94VQ4snykYvYe7sVgHIqCrIZbAYTvgCIoRYkpQ_AAjcuRt80vqJDthz76qmV-IlcEoW7hXGwcGABuM4LK0YCdyxBIVWKQQ-uwCoG3Kpey5lZwW9d2qMI7mumdNHjYHtIkkKBEvxESCTHS_EgpdofyeDwkrYLiVBCq_rNX693dwtU-8CLmvBj1AQtA6ZsCvbO4tl8eX2oKNYhcpqcb2v7ZYbV70O_js1QjChwwfQFRQg-y_N1gydHLGfQw7qRcJ5ldaO8ZXtnZ_jHCai0vNG5kv8Du7klFsdc32OVkDJIxg4gK1SIf_Ebm_xYacI0BGb5IjceJTv-S45d241wiEHBbHi4rwCBTGmXVA7iLg7ciqZJXXlypjSC7n4AnnWxpHUqNo_g0Z5wQ6yCeMkyQ0K24v9_NfygE1bB7LRcn5aYjIng4GiMGm9XHNLkernOz3wu-Qz3o0px6BesVLvFC92LjbwRB2E8A_nOytxghnAiJ4gPedsiN4QwXhTVykO0PaZjfIwqJ3o-Rge5rTL0QA9PQzplS4FlRMTyrFuYDdV5uviW7zgu_S8SIVA5B8vU06AE0gox4YlyRUta0BLoNGCdVEAA_LRhTAJ2s14IYkkhLytp0lRBkVOv9fBqnShrSSKxt5Z8d_OkJJgkAQM4RWEPegNQ85yyA3qeXA6UUh_-PodvgVTtp4idWPgg2kmIwggldY4et9o7A8Whtnjh-pzTaXuX4c-qCPjV3otaZruR5YRZao'
c = 'rOpDrh85sk0I_AnwxsF9P1ogod3MMgXKbuQMS_MC4X0LKdyBh2WNVHv4QLhBxtLp9hLy_3-9ocZSqPTyfpEywlJeyV6REtXdMrXZnDf6k1L73Kl7L8jDVc4WXNnHmeS0YpIjUshUK6MzHVZg4_UMzxSibiTxzTo3-lt3C8EL3ae55IAPm89fLnUIFZF2JVRx_Y2LZcJUJsGVACD30Cnoy3ackSfaVn3Y9ancDUQBC8BSSaFydhL4qfj2HZWP-zaWXrVztROuZLk9J_ZeZtX3SeXipo6rX8REhdWjXK-a7C0mGi2DAqo9sr-2XJsveb4r62GybSDJHgvGA2E2yd2pV8puBbJX1bAD6q3FbC5MsHCvqlrTC-Cb32FPOrBUIBUF3mMASUFa9haTLRGPr20I48e5Bh-e0cmv56TdDXLdpo1QqMCAESphObKrSBWoh1GYoOYHkd6zLDrFIHZzZ-J8X7dkoo0RllJNMIG15pQE9rT7L6AWgxP1U1s3cV-JCbk2bJFKLdNu5OKZ6LncRKN_yb2j_U21A0ZbwY1AY_RdUQpi-D5frp7xCPrlATBd3yI7gF8k2u4-V7hSTaZL2M149Cz7V4LsWPpWMrpDMhC5beHhK3wS991ozpwuuLVxT1M7ZuGFbjF9c9aG3qhCboSKwTShUUGriqv1F6SEDM4xQ-Kd7bToJhe76vCHEHVqeT-jmQtL13gNQr6eYbWYjhQZIQNlD-IUa-3x4iuABB2HT9CtNMyrWolkqURx_DYd-xt0ELj-ro48bJefhh2FXz8l6htqHSF38KaMGVAQpDeXTDw'
print(AESTest().tt(c))
