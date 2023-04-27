from encryption_and_decryption import key_generate, IP_initial_permutation, each_encryption, NIP_initial_permutation


def des_encryption(bits, key):
    """
    实现des算法的总体加密
    :return: 返回经过16轮加密的64位密文
    """
    '''产生16轮的密钥'''
    keyList = key_generate.key_generate(key)
    '''初始置换IP'''
    bits_encryption = IP_initial_permutation.IP_initial_permutation(bits)
    '''16轮加密'''
    for j in range(16):
        bits_encryption = each_encryption.encryption(bits_encryption, keyList[j])
        '''输出每个分组加密时第8轮的输出(我的学号为2021141530088，因此2021141530088 = 8 mod 16)'''
        if j == 7:
            print('第8轮的二进制码为' + bits_encryption + '\n')
    '''位置交换'''
    bits_encryption = bits_encryption[32:] + bits_encryption[:32]
    '''初始逆置换IP'''
    bits_encryption = NIP_initial_permutation.NIP_initial_permutation(bits_encryption)

    return bits_encryption
