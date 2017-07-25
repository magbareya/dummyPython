import logging
import sys

def main():
    """
    The level of logger is set to NOTSET by default, which means: take the level of parent, if it is already the root
    logger, then print all the messages.
    The function `logging.getLogger` will NOT return the root logger.
    The default of the root logger is logging.WARNING = 30
    Calling the logger with level lvl < logger.level will not invoke its handlers, even if their log_level is >= lvl.
    :return:
    """
    logger = logging.getLogger('dummy')
    logger.setLevel(1)
    logger.parent.setLevel(1)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    #logger.addHandler(handler)
    logger.log(logging.DEBUG, 'dummy message1')

    logger.log(logging.DEBUG, 'dummy message2')

if __name__ == '__main__':
    main()