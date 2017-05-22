import inspect
import sys

class A:

    def __init__(self, v):
        self._x = v


def print_var(v):
    for p in vars(v):
        if '__dic__' in dir(p):
            print_var(vars(v)[p])
        else:
            print("%s= %s" % (p, vars(v)[p]))

#TODO: add the caller name
def trace_func(frame, event, arg):
    print('event = %s'%event)
    if event == 'exception':
        print('arg = %s, %s, %s' % arg)
    else:
        print('arg = %s' % arg)
        print('file name = %s'%frame.f_code.co_filename)
    print('name = %s'%frame.f_code.co_name)
    print('line no = %s'%frame.f_lineno)
    print('_____________')
    return trace_func

def trace_specific_func(frame, event, arg):
    if event == 'call':
        print('**********')
        """info = inspect.getframeinfo(frame = frame)
        print(info)
        print(inspect.trace())"""
        stack = inspect.stack()
        for f in stack:
            print(f)
        print('_____________')
        if frame.f_code.co_name == '__init__':
            def trace_init(frame, event, arg):
                print("I'm tracing __init__")
                trace_func(frame, event, arg)
            return trace_init
        elif frame.f_code.co_name == 'f':
            def trace_f(frame, event, arg):
                print("I'm tracing f")
                trace_func(frame, event, arg)
            return trace_f
        elif frame.f_code.co_name == 'g':
            def trace_g(frame, event, arg):
                print("I'm tracing g")
                trace_func(frame, event, arg)
            return trace_g
        elif frame.f_code.co_name == 'main':
            def trace_main(frame, event, arg):
                print("I'm tracing main")
                trace_func(frame, event, arg)
            return trace_main
    else:
        return trace_func

def f(a):
    x = 5 + 7
    y = x**2
    return y

def g(x):
    a = [i**2 for i in range(10)]
    a[5] = x
    return a

    def main():
        a = A(1)
        y = f(a)
        l = g(125)
        print(y)
        print(l)

    def print(s):
        print(s)

    if __name__ == '__main__':
        sys.settrace(trace_specific_func)
        main()
