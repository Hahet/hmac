import hmac
from hashlib import sha1
import chao_hmac


def test_gen_key():
    pass


def test_hmac():
    key1 = 'Update the hmac object with the string msg. Repeated calls are equivalent to a single call with the concatenation of all the arguments'
    key2 = 'hmac'
    message = 'hello hmac'

    byte_key1 = str.encode(key1)
    byte_key2 = str.encode(key2)
    byte_msg = str.encode(message)
    excepted1 = hmac.new(byte_key1, msg=byte_msg, digestmod=sha1).hexdigest()
    excepted2 = hmac.new(byte_key2, msg=byte_msg, digestmod=sha1).hexdigest()
    result1 = chao_hmac.c_hmac(byte_key1, byte_msg).hexdigest()
    result2 = chao_hmac.c_hmac(byte_key2, byte_msg).hexdigest()

    assert excepted1 == result1, 'hmac key1'
    assert excepted2 == result2, 'hmac key2'
