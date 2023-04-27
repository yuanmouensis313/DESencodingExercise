from encryption_and_decryption import resource


def NIP_initial_permutation(bits):
    """
    对传入的64位的bits实现初始逆置换
    :param bits: 64位的bits
    :return: 返回逆置换后的64为bits
    """
    ret = ''
    for i in resource.NIP:
        ret = ret + bits[i-1]

    return ret
