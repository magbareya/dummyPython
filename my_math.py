from unittest import TestCase
from my_mathh import MyMath
import sys


class MyTests(TestCase):

    def test_with_tracer(self):
        old_tracer = sys.gettrace()

        def my_tracer(frame, event, arg):
            nonlocal old_tracer
            print('my tracer was called')
            print('event = %s' % event)
            if event == 'exception':
                print('arg = %s, %s, %s' % arg)
            else:
                print('arg = %s' % arg)
                print('file name = %s' % frame.f_code.co_filename)
            print('name = %s' % frame.f_code.co_name)
            print('line no = %s' % frame.f_lineno)
            print('_____________')
            if old_tracer is not None:
                old_tracer(frame, event, arg)
            return my_tracer

        sys.settrace(my_tracer)
        calc = MyMath()
        sys.settrace(my_tracer)
        assert calc.power(2,2) == 4
        sys.settrace(my_tracer)
        assert calc.mul(2,3) == 6
        sys.settrace(my_tracer)
