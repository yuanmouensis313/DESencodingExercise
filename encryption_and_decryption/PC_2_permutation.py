from encryption_and_decryption import resource


def PC_2_permutation(bits):
    """
    实现PC_2置换
    :param bits:
    :return:
    """
    ret = ''
    for i in resource.PC_2:
        ret = ret + bits[i-1]

    return ret
