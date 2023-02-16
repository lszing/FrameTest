import logging
import os
import random
import inspect
from logging.handlers import RotatingFileHandler
import time

log_path = os.path.dirname(os.path.abspath(__file__))
log_name = log_path + '\\case.log'

handlers = {
    logging.DEBUG: os.path.join(log_path, 'case%s.log' % ''),

    logging.INFO: os.path.join(log_path, 'case%s.log' % ''),

    logging.WARNING: os.path.join(log_path, 'case%s.log' % '.wf'),

    logging.FATAL: os.path.join(log_path, 'case%s.log' % '.wf'),

}


def createHandlers():
    logLevels = handlers.keys()
    for level in logLevels:
        path = os.path.abspath(handlers[level])
        handlers[level] = RotatingFileHandler(path, maxBytes=10000000000, backupCount=2, encoding='utf-8')
        # handlers[level] = ConcurrentRotatingFileHandler(path, "a",512*1024,5)


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


def single(log):
    _instance = {}

    def inner(a):
        if log not in _instance:
            _instance[log] = log(a)
        return _instance[log]

    return inner


# @single
# 日志类传入logid
class Log(object):
    def __init__(self, logid):
        self.logid = logid
        self.__loggers = {}
        logLevels = handlers.keys()

        for level in logLevels:
            logger = logging.getLogger(str(level))

            # 如果不指定level，获得的handler似乎是同一个handler?

            logger.addHandler(handlers[level])
            # logger.addHandler(logger)

            logger.setLevel(level)

            self.__loggers.update({level: logger})
            # print(self.__loggers)

    def setLogId(self, logId):
        if logId:
            self.logid = logId

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]

        '''日志格式：[时间] [类型] [记录代码] 信息'''

        return "[%s] -[%s - %s - %s]- logid:%s- %s: %s" % (
            self.printfNow(), filename, lineNo, functionName, self.logid, level, message)

    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def info(self, message):
        message = self.getLogMessage("info", message)

        self.__loggers[logging.INFO].info(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)

        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)

        self.__loggers[logging.DEBUG].debug(message)

    def fatal(self, message):
        message = self.getLogMessage("fatal", message)

        self.__loggers[logging.FATAL].fatal(message)

    @staticmethod
    def generatelogid():
        list = []
        for number in range(7):
            no = str(random.randint(0, 9))
            list.append(no)
        logid = ''.join(list).replace("", "")
        return logid


# 文件中直接实例化 其他文件直接导入实例
createHandlers()
#单例模式
log = Log(generatelogid())

# global logidd
# logidd = generatelogid()
# 加载模块是创建全局变量

# if __name__ == '__main__':
#     # print(os.getcwd()+'\case.log')s
#     # print(os.path.dirname(os.path.abspath(__file__)) + '\\case.log')
#     # log().info('testttttttttttttttttttttt:{}'.format('12332'))
#     # print(generatelogid())
#     loger = log(logidd)
#     loger.fatal('test')
