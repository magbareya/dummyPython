import sys
import logging


def main():
    logging.basicConfig(format=u'%(filename)s:%(lineno)d:%(levelname)s [%(asctime)s]: %(message)s')
    log = logging.getLogger('dummy')
    log.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('dummy.log')
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    #print(logging.Handler.__dict__)
    t = (5, 60, 334)
    #log.info('%d  %d  %d', *t)


if __name__ == '__main__':
    main()