import rsa
import os
import base64

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


ttttt = RsaCrypto.public_encrypt("tststs")
print(RsaCrypto.public_decrypt(ttttt))
wwww = RsaCrypto.rsa_sign('test', 'SHA-1')
print(wwww)
print(RsaCrypto.rsa_verify('test', wwww))
