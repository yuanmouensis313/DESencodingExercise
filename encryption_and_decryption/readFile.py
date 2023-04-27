def readfile(filelocation):
    """
    传入文件位置，将文件中的内容读出去
    :param filelocation: 文件的位置
    :return: 文件的内容
    """
    with open(filelocation, 'r',  encoding='utf-8') as file:
        contents = file.read()
        file.close()

    return contents

