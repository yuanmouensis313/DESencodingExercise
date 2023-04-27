import time

from encryption_and_decryption import encodeToBinary, readFile, divideBit, xor, des_encrypt, decodeToStr, des_decrypt, \
    writeFile


def CBC(plain1_location='resources/threeBody_hex.txt', key_location='resources/des_key.txt',
        IV_location='resources/des_iv.txt', cipher_location='resources/des_CBC_cipher.txt'):
    """
    使用CBC模式进行加密
    :return:
    """
    '''加密部分'''
    '''读取初始IV文件'''
    initial = readFile.readfile(IV_location)

    '''将读取到的字符串转化为二进制'''
    initial = encodeToBinary.encodeToBinary(initial)

    '''读取文件，明文内容和密钥内容'''
    print("CBC模式:\n开始读取明文")
    start_time = time.time()
    file = readFile.readfile(plain1_location)
    end_time = time.time()
    key = readFile.readfile(key_location)
    print("完成读取明文\n读取文件用时：" + str(end_time - start_time) + 's')

    '''将明文和密钥转化为2进制bit流'''
    print("开始加密！！！")
    start_time = time.time()
    bits = encodeToBinary.encodeToBinary(file)
    key = encodeToBinary.encodeToBinary(key)

    '''将明文的bit流分为64bit一组'''
    bitsList = divideBit.divide(bits, 64)

    ret = ''
    '''第一轮加密，将密文先与初始的IV异或，然后进行加密，得到明文分组'''
    E = xor.xor(initial, bitsList[0])
    C = des_encrypt.des_encryption(E, key)
    ret = ret + C

    '''剩下的多轮加密'''
    for i in range(1, int(len(bitsList))):
        E = xor.xor(bitsList[i], C)
        C = des_encrypt.des_encryption(E, key)
        ret = ret + C

    '''将加密后的bits流变为字符串'''
    ret = decodeToStr.decodeToStr(ret)
    end_time = time.time()

    print("加密完成！！！\n加密用时：" + str(end_time - start_time) + 's')

    '''将加密后的文件保存到文件中'''
    '''写入操作'''
    writeFile.writeFile(cipher_location, ret)

    '''解密部分'''
    '''读取初始IV文件'''
    IV_location = 'resources/des_iv.txt'
    initial = readFile.readfile(IV_location)

    '''将读取到的字符串转化为二进制'''
    initial = encodeToBinary.encodeToBinary(initial)

    '''密文位置'''
    cipher_location = 'resources/des_CBC_cipher.txt'

    '''初始密钥位置'''
    key_location = 'resources/des_key.txt'

    '''读取文件，密文内容和密钥内容'''
    file = readFile.readfile(cipher_location)
    key = readFile.readfile(key_location)

    '''将密文和密钥转化为2进制bit流'''
    print("开始解密!!!")
    start_time = time.time()
    bits = encodeToBinary.encodeToBinary(file)
    key = encodeToBinary.encodeToBinary(key)

    '''将密文的bit流分为64bit一组'''
    bitsList = divideBit.divide(bits, 64)

    ret = ''
    '''第一轮解密，将密文先解密后与初始的IV异或，然后得到明文分组'''
    D = des_decrypt.des_decryption(bitsList[0], key)
    M = xor.xor(initial, D)
    ret = ret + M

    '''剩下的多轮解密'''
    for i in range(1, int(len(bitsList))):
        D = des_decrypt.des_decryption(bitsList[i], key)
        M = xor.xor(bitsList[i - 1], D)
        ret = ret + M

    '''将解密后的bits流变为字符串'''
    ret = decodeToStr.decodeToStr(ret)
    # print('CBC解密结果:' + ret)
    end_time = time.time()
    print("解密完成！！！\n解密用时：" + str(end_time - start_time) + 's\n')

    '''将解密后的文件保存到文件中'''
    '''明文保存位置'''
    cipher_location = 'resources/des_CBC_plain.txt'
    '''写入操作'''
    writeFile.writeFile(cipher_location, ret)
