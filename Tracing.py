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
            log("%s= %s" % (p, vars(v)[p]))

#TODO: add the caller name
def trace_func(frame,event,arg):
    log('event = %s'%event)
    if event == 'exception':
        log('arg = %s, %s, %s' % arg)
    else:
        log('arg = %s' % arg)
        log('file name = %s'%frame.f_code.co_filename)
    log('name = %s'%frame.f_code.co_name)
    log('line no = %s'%frame.f_lineno)
    log('_____________')
    return trace_func

def trace_specific_func(frame,event,arg):
    if event == 'call':
        log('**********')
        """info = inspect.getframeinfo(frame = frame)
        log(info)
        log(inspect.trace())"""
        stack = inspect.stack()
        for f in stack:
            log(f)
        log('_____________')
        if frame.f_code.co_name == '__init__':
            def trace_init(frame, event, arg):
                log("I'm tracing __init__")
                trace_func(frame, event, arg)
            return trace_init
        elif frame.f_code.co_name == 'f':
            def trace_f(frame, event, arg):
                log("I'm tracing f")
                trace_func(frame, event, arg)
            return trace_f
        elif frame.f_code.co_name == 'g':
            def trace_g(frame, event, arg):
                log("I'm tracing g")
                trace_func(frame, event, arg)
            return trace_g
        elif frame.f_code.co_name == 'main':
            def trace_main(frame, event, arg):
                log("I'm tracing main")
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
    log(y)
    log(l)

def log(s):
    print(s)

if __name__ == '__main__':
    sys.settrace(trace_specific_func)
    main()
