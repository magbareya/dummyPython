import inspect
import sys


def trace_func(frame,event,arg):
    print('tracer was called, function name: %s, event: %s'%(frame.f_code.co_name, event))
    return trace_func


class TracingDecorator:
    def __init__(self, is_tracing=None):
        self._is_active = is_tracing

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, val):
        self._is_active = val

    def __call__(self, func, *args, **kwargs):
        if self._is_active == None:
            return sys.gettrace()
        if self._is_active:
            def traced_func(*args, **kwargs):
                tracer = sys.gettrace()
                sys.settrace(trace_func)
                func(*args, **kwargs)
                sys.settrace(tracer)
            return traced_func
        else:
            def dont_trace_func(*args, **kwargs):
                tracer = sys.gettrace()
                sys.settrace(None)
                func(*args, **kwargs)
                sys.settrace(tracer)
            return dont_trace_func


def tracing_decorator(should_trace):
    def decorator(func):
        if should_trace:
            def traced_func(*args, **kwargs):
                tracer = sys.gettrace()
                sys.settrace(trace_func)
                func(*args, **kwargs)
                sys.settrace(tracer)
            return traced_func
        else:
            def dont_trace_func(*args, **kwargs):
                tracer = sys.gettrace()
                sys.settrace(None)
                func(*args, **kwargs)
                sys.settrace(tracer)
            return dont_trace_func
    return decorator


@TracingDecorator(True)
def foo(s):
    print('foo is traced')
    hoo(s)
    print(s)


@TracingDecorator(False)
def goo(s):
    print('goo is NOT traced')
    hoo(s)
    print(s)


def hoo(s):
    print('no decorator was declared')
    print(s)


def main():
    foo("aaaa")
    goo("gggg")
    foo("ffff")
    hoo('hhhh')


if __name__ == '__main__':
    main()