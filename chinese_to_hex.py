def chineseToHex():
    """
    将读入文件中的中文转化为16进制的数据，然后写到一个新的文件中
    :return: 无返回
    """
    filelocation = 'resources/三体全集.txt'
    newfilelocation = 'resources/threeBody_hex.txt'

    '''保存读入的消息'''
    contents = ''
    '''打开文件，读数据'''
    with open(filelocation, 'r', encoding='utf-8') as file:
        contents = file.read()
        file.close()

    '''将中文转化为16进制编码'''
    contents = contents.encode('utf-8')
    ret = ''
    for i in contents:
        ret = ret + hex(i)[2:]

    '''将最后不足64bit的分组补齐'''
    l = len(ret)
    if l % 16 != 0:
        ret = ret + 'a' * (16 - l % 16)

    '''写入数据'''
    with open(newfilelocation, 'w', encoding='utf-8') as file:
        file.write(ret)
        file.close()
