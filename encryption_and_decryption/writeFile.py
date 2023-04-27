def writeFile(filelocation, message):
    """
    向制定位置写入数据
    :param message: 要写入的数据
    :param filelocation: 要写入的位置
    :return: 无返回
    """
    with open(filelocation, 'w', encoding='utf-8') as file:
        file.write(message)
        file.close()
    return 0

