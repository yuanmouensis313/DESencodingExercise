from encryption_and_decryption import f_change, xor


def encryption(bits, key):
    """
    传入64位的bits，分为2组32位，分别处理
    :param key: 传入每一轮加密的密钥，64位
    :param bits: 64位bits
    :return: 返回64位一轮加密后的bits
    """
    bits_left = bits[:32]
    bits_right = bits[32:]
    bits_f = f_change.f_change(bits_right, key)
    bits_xor = xor.xor(bits_left, bits_f)

    return bits_right + bits_xor
