def e_extend(bits):
    """
    将传入的32位bits扩展为48位
    :param bits: 32位bits
    :return: 48位bits
    """
    ret = bits[-1] + bits[0:5] + bits[3:9] + bits[7:13] + bits[11:17] + bits[15:21] + bits[19:25] + bits[23:29] + bits[27:] + bits[0]

    return ret