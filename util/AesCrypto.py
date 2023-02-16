import urllib

from Cryptodome.Cipher import AES
# from Crypto.Cipher import AES
from urllib import parse
import base64
from binascii import b2a_hex, a2b_hex

# chr() 用来标识ascii码对应的字符
# ord() 用来返回对应字符的ascii码
# BLOCK_SIZE = AES.block_size
# # 补位
# pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
# # pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * '='
# # 去除补位
# unpad = lambda s: s[:-ord(s[len(s) - 1:])]
AES_SECRET_KEY = 'abc!@#1231234567'
IV = 'abc!@#1231234567'
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


# AES加密模式：CBC
# 填充方式：PKCS5
# 偏移量：密钥截取前16位
# 输出：base64
# 字符：utf-8
# 密钥是string类型,使用时需转成bytes
# 偏移量是string类型,使用时需转成bytes
class AesCrypto:
    # CIPHER_PARAM = 'AES/CBC/PKCS5Padding'
    # md5 = hashlib.md5()
    # md5.update(.encode())
    # fansMd5 = md5.hexdigest().upper()
    #
    # # key
    # fan16 = fansMd5[0:16].encode()
    #
    # # 偏移量
    # fan32 = fansMd5[16:].encode()
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    def tt(self, s: str):
        # IV偏移量
        cipher = AES.new(self.key.encode('utf-8'), mode=self.mode, IV=IV.encode('utf-8'))
        self.ciphertext = cipher.encrypt(bytes(pad(s), encoding='utf-8'))
        # s = pad(s)
        # decoder = base64.b64decode(s)
        # s = s.replace('-', '+')
        # s = s.replace('_', '/')
        # decoder = pad(decoder)
        # print(decoder)
        # decryped_text = cipher.decrypt(decoder)
        # print(decryped_text)
        # decryped_text = decryped_text.decode('utf-8', errors='ignore')
        # result = unpad(decryped_text)
        # return base64.b64encode(self.ciphertext).decode('utf-8')
        # l = [hex(int(i)) for i in self.ciphertext]
        # result = ''.join(l)
        # 将byte数组转为16进制字符串 byte数组.hex()  对应java的是
        '''
        private static String toHexString(byte b[]) {
        StringBuilder hexString = new StringBuilder();
        for (int i = 0; i < b.length; i++) {
            String plainText = Integer.toHexString(0xff & b[i]);
            if (plainText.length() < 2){
                plainText = "0" + plainText;
            }
            hexString.append(plainText);
        }
        return hexString.toString();
        }
        '''
        # .hex()返回16进制字符串
        result = self.ciphertext.hex()
        # d5d7d5262d41f5f473081221206688d2337ccc7b026905c11226e617b6f2a107
        # print(self.ciphertext)
        return result

    def decrypt(self, text):
        # python将16位字符串转为byte数组  bytearray.fromhex(text) 等同于Java 的
        '''
         private static byte[] convertHexString(String ss) {
        byte digest[] = new byte[ss.length() / 2];
        for (int i = 0; i < digest.length; i++) {
            String byteString = ss.substring(2 * i, 2 * i + 2);
            int byteValue = Integer.parseInt(byteString, 16);
            digest[i] = (byte) byteValue;
        }
        return digest;
        }
        '''
        decode = bytearray.fromhex(text)
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV=IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text).decode('utf-8')


# c = 'test_mCgMBOeQ1JPlGTfT0pt'
# print(AesCrypto().tt(c))
a = '28c296b19b5cbdb4af96efbefa1688fe031865d977a058efe4d50251a4d692a9'
# a = 'AATpaGBFX8kkCeO1gVd/x4NAAd58/O60MKCxD/5Ad8ANYVeTsdk='
print(AesCrypto().decrypt(a))
if __name__ == '__main__':
    #
    def twoscomplement_to_unsigned(i):
        return i % 256


    # b = [118, -86, -46, -63, 100, -69, -30, -102, -82, -44, -40, 92, 0, 98, 36, -94]
    b = [48, -126, 2, 92, 2, 1, 0, 2, -127, -127, 0, -103, 54, -112, 60, -20, -92, -38, -22, 39, -3, 50, 19, -80, 10, -96, -66, 35, -25, 24, 28, 26, -96, -55, 32, 1, -87, 106, 59, -85, 93, 22, -8, -37, 114, 72, -30, 74, 115, -26, 65, 24, 6, 27, 30, -24, -63, -77, -48, 70, 99, 92, -17, -41, 100, -31, 35, 35, -20, -39, 101, 95, 53, 51, -47, 79, -117, 8, 120, -65, -86, -23, -68, -57, -92, -126, 113, -40, -61, 74, 42, -75, -8, 43, -53, -83, -66, 76, 32, 25, 10, -69, 123, -33, 65, -99, -64, 97, -110, 103, 9, 25, 28, 120, 24, 100, 23, -115, 108, 53, 10, -67, 119, 80, -31, 11, -96, 49, -26, 54, 101, 103, 92, -87, -54, -11, 73, 97, -37, 2, 3, 1, 0, 1, 2, -127, -128, 29, -10, -74, -44, -61, 111, 38, 69, 31, 22, -4, -127, 47, 47, -108, -22, 58, -71, 74, 84, -52, -68, 95, 57, 60, 57, -10, -59, -66, -88, -47, 2, 80, 96, -108, 114, 117, 31, 31, -117, -31, 119, -24, 59, -18, 71, 91, -76, 66, -33, -47, -32, 50, 30, -49, -115, 0, -52, -92, 99, -105, -16, 30, -74, -27, -19, 127, 22, 113, 48, 60, 58, 104, -28, 58, 4, -23, 120, -29, 102, 22, -63, 41, -35, 94, 103, -38, 123, 40, -107, 92, -72, 92, 48, 104, -45, 98, 64, -16, 36, 115, -20, -75, -96, -56, 51, 93, -126, 121, -39, -16, -59, -10, -3, -11, 117, -110, -111, 21, 98, 93, -19, 95, -104, -79, -33, 0, 121, 2, 65, 0, -39, 35, -59, 90, 56, -45, 85, 108, 112, 44, -28, -110, -128, 75, -24, 91, -4, -15, 55, -68, 78, -123, 34, 57, 14, 34, 22, 42, 45, 4, -87, -95, -93, -6, 103, -81, -118, -50, -59, -78, 19, -73, -93, 11, -71, 68, 42, -10, -82, -10, -99, 15, -13, 35, -80, -51, -66, 9, 15, 19, -22, -28, -23, -59, 2, 65, 0, -76, -94, 0, -3, 1, 119, 56, 16, 62, -111, 77, -22, 118, 2, -42, -28, 120, -121, 28, 91, 27, 33, 25, 16, -117, -45, -65, 89, -96, -91, 101, 3, -89, -83, 41, 83, -123, -59, -122, -45, -28, 80, -77, -105, -61, 74, -40, 23, -119, 104, -22, 53, 103, -64, -107, -36, -97, -91, 6, -105, 34, 52, -9, 31, 2, 64, 6, 72, 42, -91, 121, -113, 99, -95, 71, 125, -124, -1, 88, 6, -38, 42, 15, 31, 75, 101, 127, 64, 10, -59, 107, -53, 64, -88, -25, -76, -126, -45, -46, 82, -92, 61, 71, -34, -61, -119, 107, 88, -100, -74, -14, 29, 46, -63, 4, 62, -50, 60, 111, -28, 80, 113, 35, 86, 79, -63, 91, -62, 83, -95, 2, 64, 61, 12, -68, 20, -58, -40, 10, 100, -61, 32, -51, 26, -65, 67, -6, 105, 65, -85, 56, -108, 58, 57, 23, -123, -106, 28, -67, 1, -121, -32, 30, -95, -5, -101, -12, -23, -69, -66, -92, -15, 28, -85, -127, -25, 123, 35, -30, -95, 33, -38, 9, -66, 127, 16, -126, 22, 13, 6, -13, -111, 69, 8, 109, -75, 2, 65, 0, -122, 46, -126, 96, 61, -114, 29, 98, -93, 14, -106, 103, 108, -99, 110, 123, 125, 56, 98, 29, -52, -70, 34, 21, 42, -57, -22, -94, -1, -117, 112, -42, 70, 116, -38, -124, 2, -46, -25, 48, 115, -116, -46, -101, -11, -66, -94, 97, -43, -120, -77, 36, -24, 61, -46, -27, -81, 115, -89, 58, 28, -99, 98, -78]
    result = bytes(map(twoscomplement_to_unsigned, b))
    print(f'result is {result}')
    iv_byte = bytes(i % 256 for i in b)
    print(f'iv_byte is {iv_byte.hex()}')

    # bytes from str
    testStr = 'abc'
    print(bytes(testStr, 'utf-8'))

    # bytes from iterable
    # by = bytes([1, 2, 16, 17, 102])
    # print(by)
    # print(f'b.hex() is {by.hex()}')
