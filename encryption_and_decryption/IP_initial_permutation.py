from encryption_and_decryption import resource


def IP_initial_permutation(bits):
    """
    对传入的64位的bit流实现初始置换
    :param bits: 64位的01bit流
    :return:置换后的01bit流
    """
    newbits = ''
    for i in resource.IP:
        newbits = newbits + bits[i-1]
    
    return newbits
