from encryption_and_decryption import E_extend, xor, s_search
from encryption_and_decryption.p_permutation import p_permutation


def f_change(bits, key):
    """
    传入32位的bits和这一轮函数的key，实现加密
    :param bits: 32位的bits
    :param key: 48位的key
    :return: 32位的加密bits
    """
    '''对32位的bits进行E-扩展'''
    bits = E_extend.e_extend(bits)
    '''将两个48位的bits和key进行异或运算'''
    bits = xor.xor(bits, key)
    '''将异或后的结果分为8组，经过s盒的运算'''
    ret = ''
    for i in range(8):
        ret = ret + s_search.search(bits[i * 6:i * 6 + 6], i)
    '''经过P置换'''
    ret = p_permutation(ret)
    return ret
