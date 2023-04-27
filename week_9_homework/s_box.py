from encryption_and_decryption import encodeToBinary, s_search, decodeToStr
from encryption_and_decryption.p_permutation import p_permutation


def s_box():
    bits = encodeToBinary.encodeToBinary('70a990f5fc36')
    print(bits)
    ret = ''
    for i in range(8):
        ret = ret + s_search.search(bits[i * 6:i * 6 + 6], i)
    print(ret)
    ret = decodeToStr.decodeToStr(ret)
    print(ret)

    bits1 = '101010101010101010101010101010101010101010101010'
    ret1 = ''
    for i in range(8):
        ret1 = ret1 + s_search.search(bits1[i * 6:i * 6 + 6], 0)
    ret1 = p_permutation(ret1)
    print(ret1)
    ret1 = decodeToStr.decodeToStr(ret1)
    print(ret1)