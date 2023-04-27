import time

from encryption_and_decryption import readFile, encodeToBinary, divideBit, des_encrypt, xor, decodeToStr, writeFile


def OFB(plain1_location='resources/threeBody_hex.txt', key_location='resources/des_key.txt',
        IV_location='resources/des_iv.txt', cipher_location='resources/des_OFB_cipher.txt'):
    """
    使用OFB模式进行加密和解密
    :return: 无返回
    """

    '''加密部分'''
    '''读取初始IV文件'''
    IV_location = 'resources/des_iv.txt'
    initial = readFile.readfile(IV_location)

    '''将读取到的字符串转化为二进制'''
    initial = encodeToBinary.encodeToBinary(initial)

    '''读取文件，明文内容和密钥内容'''
    print("OFB模式:\n开始读取明文")
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

    '''将明文的bit流分为32bit一组'''
    bitsList = divideBit.divide(bits, 32)

    ret = ''
    '''第一轮加密，先将初始向量加密后与第一组的明文分组进行异或，得到密文'''
    E = des_encrypt.des_encryption(initial, key)
    C = xor.xor(bitsList[0], E)
    ret = ret + C

    '''后面几轮加密'''
    for i in range(1, int(len(bitsList))):
        E = des_encrypt.des_encryption(E, key)
        C = xor.xor(bitsList[i], E)
        ret = ret + C

    '''将bits流转化为字符串'''
    ret = decodeToStr.decodeToStr(ret)
    # print('OFB加密结果:' + ret)

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
    cipher_location = 'resources/des_OFB_cipher.txt'

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

    '''将密文的bit流分为32bit一组'''
    bitsList = divideBit.divide(bits, 32)

    ret = ''
    '''第一轮解密，先将初始向量加密，然后与第一组密文进行异或，得到明文分组'''
    E = des_encrypt.des_encryption(initial, key)
    M = xor.xor(bitsList[0], E)
    ret = ret + M

    '''后面几轮解密'''
    for i in range(1, int(len(bitsList))):
        E = des_encrypt.des_encryption(E, key)
        M = xor.xor(bitsList[i], E)
        ret = ret + M

    '''将解密后的bits流变为字符串'''
    ret = decodeToStr.decodeToStr(ret)
    # print('OFB解密结果:' + ret)

    end_time = time.time()
    print("解密完成！！！\n解密用时：" + str(end_time - start_time) + 's\n')

    '''将解密后的文件保存到文件中'''
    '''明文保存位置'''
    cipher_location = 'resources/des_OFB_plain.txt'
    '''写入操作'''
    writeFile.writeFile(cipher_location, ret)
