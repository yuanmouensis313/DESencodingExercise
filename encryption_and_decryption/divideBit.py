def divide(bits, size=64):
    """
    实现bit流的分组,默认为64个一组
    :param bits:传入01bit流
    :param size:分组大小，默认为64
    :return:返回分组后的列表
    """
    return [bits[i: i+size] for i in range(0, len(bits), size)]
