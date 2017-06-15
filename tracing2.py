import inspect
import sys


def func1(s):
    result = 'func1 was called with ' + s
    result = func2(result)
    return result


def func2(s):
    result = 'func2 was called with ' + s
    return result


def my_tracer(frame, event, arg):
    def line_tracer(frame, event, arg):
        print('line tracer: ', frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name,
              arg, frame.f_back)
        info = inspect.getframeinfo(frame)
        m = inspect.getmodule(frame.f_code.co_filename)
        print('module = ', m)
        return line_tracer
    print("my tracer")
    stack = inspect.stack()
    for f in stack:
        print(f)
    print('-' * 20)
    print()
    return line_tracer


def main():
    s = {1,2}
    s.add(1)
    s.add(1)
    print(s)
    func1('a')
    pass


if __name__ == '__main__':
    sys.settrace(my_tracer)
    main()
