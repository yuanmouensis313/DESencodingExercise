def hex_to_chinese():
    """
    将16进制字符串转化为中文
    :return: 无返回
    """
    filelocation = 'resources/des_CBC_cipher.txt'
    newfilelocation = 'resources/hex_to_chinese.txt'

    '''保存读入的消息'''
    contents = ''
    '''打开文件，读数据'''
    with open(filelocation, 'r', encoding='utf-8') as file:
        contents = file.read()
        file.close()

    '''保存转化后的中文'''
    ret = ''
    '''每6个转化为一个中文'''
    str = '\\'
    l = len(contents)
    for i in range(int(l)):
        if i + 1 % 6 != 0:
            if i + 1 % 2 == 0:
                str = str + '\\x' + contents[i]
            else:
                str = str + contents[i]
        elif i + 1 % 6 == 0 & i != 0:
            ret = bytes(str, 'utf-8').decode()
            str = ''

    '''写入数据'''
    with open(newfilelocation, 'w', encoding='utf-8') as file:
        file.write(ret)
        file.close()
