
#加密算法
def encrypt(str):
    s=''
    for i in str:
        s+=chr(ord(i)>>1)
    return s
#解密
def decrypt(str):
    s=''
    for i in str:
        s += chr(ord(i) << 1)
    return s
enc_str=encrypt("我是你爸爸")
print(enc_str)

dec_str=decrypt(enc_str)
print(dec_str)