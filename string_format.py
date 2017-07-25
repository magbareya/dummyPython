import sys

class A:

    def call_func_by_name(self, a, b):
        function_name = 'powerr'
        func = getattr(self.__class__, function_name)
        if func is None:
            print('None')
        else:
            print(func(self, a, b))

    def power(self, a, b):
        return a**b


def main():
    a = A()
    a.call_func_by_name(2, 4)

if __name__ == '__main__':
    main()
