import time

from encryption_and_decryption import decodeToStr, des_decrypt, divideBit, des_encrypt, encodeToBinary, readFile, \
    writeFile


def ECB(plain1_location='resources/threeBody_hex.txt', key_location='resources/des_key.txt',
        IV_location='resources/des_iv.txt', cipher_location='resources/des_ECB_cipher.txt'):
    """
    使用ECB进行加密和解密
    :return: 无返回
    """

    """加密部分"""

    '''读取文件，明文内容和密钥内容'''
    print("ECB模式:\n开始读取明文")
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

    '''分组进行加密，每组都为64bit'''
    ret = ''
    for i in range(int(len(bitsList))):
        ret = ret + des_encrypt.des_encryption(bitsList[i], key)
    ret = decodeToStr.decodeToStr(ret)
    # print('ECB加密结果:' + ret)
    end_time = time.time()
    print("加密完成！！！\n加密用时：" + str(end_time - start_time) + 's')

    '''将加密后的文件保存到文件中'''
    '''写入操作'''
    writeFile.writeFile(cipher_location, ret)

    """解密部分"""
    '''密文位置'''
    cipher_location = 'resources/des_ECB_cipher.txt'

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
    '''分组进行加密，每组都为64bit'''
    ret = ''
    for i in range(int(len(bitsList))):
        ret = ret + des_decrypt.des_decryption(bitsList[i], key)
    ret = decodeToStr.decodeToStr(ret)
    end_time = time.time()
    print("解密完成！！！\n解密用时：" + str(end_time - start_time) + 's\n')

    # print('ECB解密结果:' + ret)

    '''将解密后的文件保存到文件中'''
    '''明文保存位置'''
    cipher_location = 'resources/des_ECB_plain.txt'
    '''写入操作'''
    writeFile.writeFile(cipher_location, ret)
