'''
hmac 是一个利用现有的摘要算法（md5 sha1 sha512 等）来生成 MAC 的算法
'''


from hashlib import sha1
import hmac


def gen_key(b):
    #  根据s求bytes长度为block_size的key

    block_size = sha1().block_size
    # b = str.encode(s)
    d = block_size - len(b)
    if d > 0:
        b = b + b'\0' * d
    else:
        b = sha1(b).digest()
        l = len(b)
        if len(b) < block_size:
            b = b + b'\0' * (block_size - len(b))
    return b


def pads(byte_key: bytes):
    K = byte_key
    o = 0x5c
    i = 0x36
    outer_pad = b''
    inner_pad = b''
    for a in K:
        oa = bytes([o ^ a])
        ia = bytes([i ^ a])
        outer_pad = outer_pad + oa
        inner_pad = inner_pad + ia
    return inner_pad, outer_pad


def c_hmac(key: bytes, message: bytes):
    K = gen_key(key)
    inner_pad, outer_pad = pads(K)
    # msg = str.encode(message)
    inner = sha1(inner_pad + message)
    outer = outer_pad + inner.digest()
    h = sha1(outer)
    return h


# 在原版 hmac 的计算公式上增加了一个 b'gua' 如下
# sha1(b'gua' + outer_pad + sha1(inner_pad + message))
# key = b'a'
# msg = b'a'

print(c_hmac(b'a', b'a').hexdigest())
