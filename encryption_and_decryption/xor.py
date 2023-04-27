def xor(bits1, bits2):
    """
    对传入的两个01bits做异或运算，传入的字符长度必须相同
    :param bits1: 传入bits1
    :param bits2: 传入bits2
    :return: 返回做了异或运算后的结果
    """

    ret = ''
    for i in range(len(bits1)):
        ret = ret + str(int(bits1[i]) ^ int(bits2[i]))
    return ret

