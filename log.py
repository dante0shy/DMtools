import logging
import logging.handlers

class LogMessage:

    def __init__(self,LOG_text):

        LOG_FILE = 'DMlittle.log'

        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

        formatter = logging.Formatter(fmt)  # 实例化formatter
        handler.setFormatter(formatter)  # 为handler添加formatter

        logger = logging.getLogger('tst')  # 获取名为tst的logger
        logger.addHandler(handler)  # 为logger添加handler
        logger.setLevel(logging.DEBUG)
        print(LOG_text)
        logger.info(LOG_text)


#LogMessage('aaa')