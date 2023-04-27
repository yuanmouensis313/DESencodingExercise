from encryption_and_decryption import resource


def PC_1_permutation(bits):
    """
    实现PC_1置换
    :param bits:传入的初始密钥,为64位
    :return: 返回56位的01bit流，去除了奇偶校验位
    """
    ret = ''
    for i in resource.PC_1:
        ret = ret + bits[i - 1]

    return ret
