from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
from MultipleInterfaceManager.settings import PRPCRYPT_KAY_SALT
AES_LENGTH = 16
key = PRPCRYPT_KAY_SALT
class prpcrypt():
    def __init__(self):
        self.key = key
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.pad_key(self.key).encode(), self.mode)

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    # 加密内容需要长达16位字符，所以进行空格拼接
    def pad(self,text):
        while len(text) % AES_LENGTH != 0:
            text += ' '
        return text

    # 加密密钥需要长达16位字符，所以进行空格拼接
    def pad_key(self,key):
        while len(key) % AES_LENGTH != 0:
            key += ' '
        return key

    def encrypt(self, text):

        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        # 加密的字符需要转换为bytes
        # print(self.pad(text))
        self.ciphertext = self.cryptor.encrypt(self.pad(text).encode())
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt(self, text):
        plain_text = self.cryptor.decrypt(a2b_hex(text)).decode()
        return plain_text.rstrip(' ')


if __name__ == '__main__':
    pc = prpcrypt()  # 初始化密钥
    e = pc.encrypt("0123456789ABCDEF")
    d = pc.decrypt(e)
    print(e)
    print(d)
    e = pc.encrypt("00000000000000000000000000")
    print(type(e))
    ca = b'8f55cdb828ce3a984bdeedc6a5553699'
    print(type(ca))
    d = pc.decrypt(ca)
    print(d)
    print("AAAAAAAAAAAAAAAAAAAA")
    e = pc.encrypt("YQC*&!@@#")
    d = pc.decrypt(e)
    print(e)
    print()
