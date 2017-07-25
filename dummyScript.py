import sys
import os
import logging
import inspect

class Foo:
    def foo(self):
        def goo():
            pass
        return goo


class A:
    def __init__(self):
        self._member = "A"

    def foo(self):
        print(self._member)

    def return_func(self):
        return self.foo

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        self._member = value


def log():
    logging.basicConfig(format=u'%(filename)s:%(lineno)d:%(levelname)s [%(asctime)s]: %(message)s')
    log = logging.getLogger('dummy')
    log.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('dummy.log')
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    #print(logging.Handler.__dict__)
    t = (5, 60, 334)
    #log.info('%d  %d  %d', *t)


def fullname(o):
    return o.__module__ + "." + o.__class__.__module__ + "." + o.__name__


def foo():
    frame = inspect.stack()[1]
    print(frame.lineno)
    print(frame)

def goo():
    foo()

def format_msg():
    return '{a}, {b}'.format(a='1', b='2')


def main():
    m = '{a}, {b}'.format(a='1', b='2')
    print(format_msg())

if __name__ == '__main__':
    main()
