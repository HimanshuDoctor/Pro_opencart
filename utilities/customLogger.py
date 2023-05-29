import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=path)

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

