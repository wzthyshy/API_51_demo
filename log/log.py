"""
日志配置
"""
import logging
import os
import datetime

CHECK_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 定义日志文件路径
LOG_PATH = os.path.join(CHECK_PATH, "log")



class Logger():

    def __init__(self, name="logs"):
        self.logname = name + "_" + str(datetime.date.today()) + ".log"
        # self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%M%D")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")
