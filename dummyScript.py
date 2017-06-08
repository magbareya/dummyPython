import sys
import logging


def main():
    logging.basicConfig(format=u'%(filename)s:%(lineno)d:%(levelname)s [%(asctime)s]: %(message)s')
    log = logging.getLogger('Tracing')
    log.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('Tracing.log')
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    t = (5, 60, 334)

    log.info('%d  %d  %d', *t)


if __name__ == '__main__':
    main()