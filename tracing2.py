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
              arg)
        return line_tracer
    info = inspect.getframeinfo(frame=frame)
    print(info)
    print()
    for f in inspect.stack():
        print(f)
    print('-' * 20)
    print()
    print (info == inspect.stack()[1])
    return line_tracer


def main():
    func1('a')
    pass


if __name__ == '__main__':
    sys.settrace(my_tracer)
    main()
