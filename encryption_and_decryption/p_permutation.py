from encryption_and_decryption import resource


def p_permutation(bits):
    """
    完成p置换,输入32位
    :return: 返回32位的Bits
    """
    ret = ''
    for i in resource.p:
        ret = ret + bits[i - 1]

    return ret
