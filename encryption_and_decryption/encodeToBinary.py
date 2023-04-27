def encodeToBinary(s: str):
    """
    将传入的字符按照规则变为01bit流
    :param s:传入的字符串
    :return:01bit流
    """
    '''将字符串每一个都转化为bytes类型，将bytes类型强转为int类型，利用bin()函数将其转化为01bit流'''
    ret = ''
    for i in s:
        '''每一个我们都对其进行右对齐并补齐8位'''
        bc = bin(int(bytes(i, 'utf=8'), 16))[2:].rjust(4, '0')
        ret = ret + bc

    return ret

