from encryption_and_decryption import PC_1_permutation, bits_ring_shift_left, resource, PC_2_permutation


def key_generate(key):
    """
    传入初始的key值,生成16轮加密的密钥
    :param key:初始的64位的密钥
    :return:16轮的密钥
    """
    '''用来存放16轮的结果'''
    key_list = ['' for i in range(16)]
    '''对密钥进行PC-1置换'''
    key = PC_1_permutation.PC_1_permutation(key)
    '''分为两组'''
    key_left = key[:28]
    key_right = key[28:]
    '''16次'''
    for i in range(16):
        '''循环左移'''
        key_left = bits_ring_shift_left.ring_shift_left(key_left, resource.LS[i])
        key_right = bits_ring_shift_left.ring_shift_left(key_right, resource.LS[i])
        '''左右合并调用置换PC_2,并存入key_list中'''
        key_list[i] = PC_2_permutation.PC_2_permutation(key_left + key_right)

    return key_list
