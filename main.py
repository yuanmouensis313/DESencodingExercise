import ECB
import CBC
import CFB
import OFB
import chinese_to_hex
import time
import hex_to_chinese
from week_9_homework import s_box
import sys

if __name__ == '__main__':
    start_time = time.time()
    chinese_to_hex.chineseToHex()
    end_time = time.time()
    print("将中文转化为16进制用时:" + str(end_time-start_time) + "s")

    hex_to_chinese.hex_to_chinese()
    s_box.s_box()

    if len(sys.argv) == 1:
        print('没有指定模式,默认为四种都执行')
        CFB.CFB()
        OFB.OFB()
        ECB.ECB()
        CBC.CBC()
    elif len(sys.argv) == 6:
        if sys.argv[4] == 'CFB':
            CFB.CFB(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
        elif sys.argv[4] == 'OFB':
            OFB.OFB(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
        elif sys.argv[4] == 'ECB':
            ECB.ECB(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
        elif sys.argv[4] == 'CBC':
            CBC.CBC(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])



