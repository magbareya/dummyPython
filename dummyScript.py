import sys
import logging


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


def main():
    a = A()
    f = a.return_func()
    f()
    a.member = "B"
    f()
    pass

if __name__ == '__main__':
    main()
