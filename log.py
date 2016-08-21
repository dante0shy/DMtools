import logging
import logging.handlers

#Log tool to write the error log

class LogMessage:

    def __init__(self,LOG_text):

        LOG_FILE = 'DMtools.log'

        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        logger = logging.getLogger('tst')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        print(LOG_text)
        logger.info(LOG_text)


#LogMessage('aaa')