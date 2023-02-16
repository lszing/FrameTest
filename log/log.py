import logging
import os
import random


class MyFilter(logging.Filter):
    logid = ""

    def filter(self, record):
        record.logid = self.logid
        return True


def generatelogid():
    list = []
    for number in range(7):
        no = str(random.randint(0, 9))
        list.append(no)
    logid = ''.join(list).replace("", "")
    return logid

#日志类传入logid
class test_log:
    def __init__(self, logid):
        self.logid = logid
    # @staticmethod
    def log(self):
        logger = logging.getLogger()
        # 大于等于info级别日志才会打印

        logger.setLevel(logging.INFO)
        logger.handlers.clear()
        # 获取当前函数所在路径
        myfilter_ = MyFilter()
        # logidd = generatelogid()
        logger.addFilter(myfilter_)
        myfilter_.logid = self.logid
        log_path = os.path.dirname(os.path.abspath(__file__))
        log_name = log_path + '\\case.log'
        # if not logger.handlers:
        fh = logging.FileHandler(log_name, mode='a', encoding="utf-8")
        # 定义日志输出格式
        # -%(module)s%-(filename)s-%(funcName)s
        formatter = logging.Formatter(
            "%(asctime)s - %(pathname)s[line:%(lineno)d] -logid:%(logid)s- %(levelname)s: %(message)s")
        # formatter = logging.Formatter("-%(logid)s-")
        fh.setFormatter(formatter)
        # 将logger添加都handler中
        logger.addHandler(fh)
        return logger


global logidd
logidd = generatelogid()

if __name__ == '__main__':
    print(os.getcwd()+'\case.log')
    print(os.path.dirname(os.path.abspath(__file__)) + '\\case.log')
    # log().info('testttttttttttttttttttttt:{}'.format('12332'))
    print(generatelogid())
