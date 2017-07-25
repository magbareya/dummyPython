import inspect
import sys
import traceback
import myModule


class A:

    def __init__(self, v):
        self._x = v


def print_var(v):
    for p in vars(v):
        if '__dic__' in dir(p):
            print_var(vars(v)[p])
        else:
            print("%s= %s" % (p, vars(v)[p]))


def trace_func(frame, event, arg):
    print('event = %s'%event)
    if event == 'exception':
        print('type =', arg[0])
        print('message =', arg[1])
        print(arg[2])
    else:
        print('arg = %s' % str(arg))
        print('file name = %s'%frame.f_code.co_filename)
    print('name = %s'%frame.f_code.co_name)
    print('line no = %s'%frame.f_lineno)
    print('locals = %s'%frame.f_locals)
    print('')
    print('_' * 20)
    return trace_func


def trace_specific_func(frame, event, arg):
    if event == 'call' or event == 'c_call':
        print('call event')
        print('locals = %s' % frame.f_locals)
        print('line no = %s' % frame.f_lineno)
        print('co code = %s' % frame.f_code.co_code)
        print('arg = ', arg)
        print('*'*10)
    return trace_func


def foo(f):
    x = f + 1
    y = x**2
    return y


def goo(g):
    x = foo(g)
    y = x**2
    raise ValueError('error message')


def double_return():
    return 3, 4


def factorial(n):
    return myModule.factorial(n)

def main():
    print(factorial(4))

    return


if __name__ == '__main__':
    sys.settrace(trace_specific_func)
    main()
