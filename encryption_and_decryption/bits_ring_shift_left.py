def ring_shift_left(bits, num):
    """
    实现bit流的循环左移
    :param bits: bit流
    :param num: 循环左移次数
    :return: 返回循环左移后的bit流
    """
    return bits[num:] + bits[:num]

