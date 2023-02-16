import rsa
import os
import base64
import hashlib
# from Cryptodome.Cipher import
# from pycryptodome import
from binascii import b2a_hex, a2b_hex
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import re

# from Crypto.PublicKey import RSA

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
save_path = path + '/lib/rsaKey/'

with open(file=save_path + 'PriKey.pem', mode='r') as f:
    priK = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(priK.encode())

with open(file=save_path + 'pubKey.pem', mode='r') as f:
    pubK = f.read()
    public_key = rsa.PrivateKey.load_pkcs1(pubK.encode())

class RsaCrypto:

    def __init__(self, PriKeyPemName='***.pem'):
        with open(file=save_path + PriKeyPemName, mode='r') as f:
            priK = f.read()
            self.private_key = rsa.PrivateKey.load_pkcs1(priK.encode())

    def generate_ras_key(self):
        (pubKey, prikey) = rsa.newkeys(1024)
        with open(file=save_path + 'pubKey.pem', mode='w+') as f:
            f.write(pubKey.save_pkcs1().decode())
        with open(file=save_path + 'priKey.pem', mode='w+') as f:
            f.write(prikey.save_pkcs1().decode())

    def public_encrypt(self, data: str) -> bytes:
        crypt_data = rsa.encrypt(data.encode('utf-8'), public_key)
        return crypt_data

    def public_decrypt(self, data: bytes) -> str:
        decrypt_data = rsa.decrypt(data, self.private_key).decode('utf-8')
        return decrypt_data

    def public_decrypt1(self, data: bytes) -> str:
        # RSA.import
        decrypt_data = rsa.decrypt(data, self.private_key).decode('utf-8')
        return decrypt_data

    '''
    hash_name:
        'MD5', 'SHA-1','SHA-224', SHA-256', 'SHA-384' or 'SHA-512'
    '''

    def rsa_sign(self, signstr: str, hash_method: str) -> bytes:
        crypt_sign = rsa.sign(signstr.encode('utf-8'), self.private_key, hash_method)
        return crypt_sign

    def rsa_verify(self, data: str, signedData: bytes) -> str:
        hash_name = rsa.verify(data.encode('utf-8'), signedData, public_key)
        return hash_name


# ttttt = RsaCrypto.public_encrypt("tststs")
# print(RsaCrypto.public_decrypt(ttttt))
# wwww = RsaCrypto.rsa_sign('test', 'SHA-1')
# # print(wwww)
# # print(RsaCrypto.rsa_verify('test', wwww))
#
# #chr() 用来标识ascii码对应的字符
# #ord() 用来返回对应字符的ascii码
# BLOCK_SIZE = AES.block_size
# # 补位
# pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
# # pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * '='
# # 去除补位
# unpad = lambda s: s[:-ord(s[len(s) - 1:])]
#
# #AES加密模式：CBC
# #填充方式：PKCS5
# #偏移量：密钥截取前16位
# #输出：base64
# #字符：utf-8
# #密钥是string类型,使用时需转成bytes
# #偏移量是string类型,使用时需转成bytes
# class AESTest:
#     CIPHER_PARAM = 'AES/CBC/PKCS5Padding'
#
#     jd = 'jdfans'
#     md5 = hashlib.md5()
#     md5.update(jd.encode())
#     jdfansMd5 = md5.hexdigest().upper()
#
#     # key
#     jdfan16 = jdfansMd5[0:16].encode()
#
#     # 偏移量
#     jdfan32 = jdfansMd5[16:].encode()
#
#     def tt(self, s: str):
#         print(self.jdfan16)
#         print(self.jdfan32)
#         #IV偏移量
#         cipher = AES.new(self.jdfan16, mode=AES.MODE_CBC, IV=self.jdfan32)
#         # s = pad(s)
#         decoder = base64.b64decode(s)
#         # s = s.replace('-', '+')
#         # s = s.replace('_', '/')
#         decoder = pad(decoder)
#         print(decoder)
#         decryped_text = cipher.decrypt(decoder)
#         print(decryped_text)
#         decryped_text = decryped_text.decode('utf-8', errors='ignore')
#         # result = unpad(decryped_text)
#         return decryped_text
#
#
# c = 'rOpDrh85sk0I_AnwxsF9P1ogod3MMgXKbuQMS_MC4X0LKdyBh2WNVHv4QLhBxtLp9hLy_3-9ocZSqPTyfpEywlJeyV6REtXdMrXZnDf6k1L73Kl7L8jDVc4WXNnHmeS0YpIjUshUK6MzHVZg4_UMzxSibiTxzTo3-lt3C8EL3ae55IAPm89fLnUIFZF2JVRx_Y2LZcJUJsGVACD30Cnoy3ackSfaVn3Y9ancDUQBC8BSSaFydhL4qfj2HZWP-zaWXrVztROuZLk9J_ZeZtX3SeXipo6rX8REhdWjXK-a7C0mGi2DAqo9sr-2XJsveb4r62GybSDJHgvGA2E2yd2pV8puBbJX1bAD6q3FbC5MsHCvqlrTC-Cb32FPOrBUIBUF3mMASUFa9haTLRGPr20I48e5Bh-e0cmv56TdDXLdpo1QqMCAESphObKrSBWoh1GYoOYHkd6zLDrFIHZzZ-J8X7dkoo0RllJNMIG15pQE9rT7L6AWgxP1U1s3cV-JCbk2bJFKLdNu5OKZ6LncRKN_yb2j_U21A0ZbwY1AY_RdUQpi-D5frp7xCPrlATBd3yI7gF8k2u4-V7hSTaZL2M149Cz7V4LsWPpWMrpDMhC5beHhK3wS991ozpwuuLVxT1M7ZuGFbjF9c9aG3qhCboSKwTShUUGriqv1F6SEDM4xQ-Kd7bToJhe76vCHEHVqeT-jmQtL13gNQr6eYbWYjhQZIQNlD-IUa-3x4iuABB2HT9CtNMyrWolkqURx_DYd-xt0ELj-ro48bJefhh2FXz8l6htqHSF38KaMGVAQpDeXTDw'
# print(AESTest().tt(c))


if __name__ == '__main__':
    pass