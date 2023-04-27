from encryption_and_decryption import IP_initial_permutation, key_generate, each_encryption, NIP_initial_permutation


def des_decryption(bits, key):
    """
    实现des的总体加密
    :param bits: 传入64位的明文
    :param key: 传入初始的密钥
    :return: 返回加密后的64位信息
    """
    '''产生16轮的密钥'''
    keyList = key_generate.key_generate(key)
    ret = ''
    '''初始置换IP'''
    bits_encryption = IP_initial_permutation.IP_initial_permutation(bits)
    '''16轮加密'''
    for j in range(16):
        bits_encryption = each_encryption.encryption(bits_encryption, keyList[15 - j])
    '''位置交换'''
    bits_encryption = bits_encryption[32:] + bits_encryption[:32]
    '''初始逆置换IP'''
    bits_encryption = NIP_initial_permutation.NIP_initial_permutation(bits_encryption)

    return bits_encryption
