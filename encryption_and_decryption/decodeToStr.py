def decodeToStr(bits):
    """
    将传入的01bits流转化为字符串，比特流长度必须被4整除
    :param bits: 传入的bits流
    :return: 返回的字符串
    """
    ret = ''
    for i in range(int(len(bits)/4)):
        ret = ret + hex(int(bits[i*4:i*4 + 4], 2))[2:]
    return ret

