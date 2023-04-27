from encryption_and_decryption import resource


def search(bits, i):
    """
    查找s盒，传入6位的bits，变为4位的bits
    :param bits: 6位的bits
    :param i: 决定第几个s盒
    :return: 4位bits
    """
    row = int(bits[0]+bits[5], 2)
    column = int(bits[1:5], 2)
    num = bin(resource.s[i][row * 16 + column])[2:].rjust(4, '0')
    return num
