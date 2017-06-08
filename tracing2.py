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
        print('line tracer: ', frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name, arg)
        return line_tracer

    if frame.f_code.co_name == 'func1':
        print('frame tracer, returning None: ', frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name, arg)
        return None
    else:
        print('frame tracer, returning line_tracer: ', frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name, arg)
        return line_tracer


def main():
    sys.settrace(my_tracer)
    func1('Mahmoud')


if __name__ == '__main__':
    main()
