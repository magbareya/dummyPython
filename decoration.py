import inspect

def our_decorator(func):
    def function_wrapper(*args, **keys):
        print(args)
        print(keys)
        f = inspect.currentframe()
        print(f.f_code.co_name)
        return func(*args, **keys)
    print("decorator was called on function %s"%func.__name__)
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    return function_wrapper

@our_decorator
def printMsg():
    print("hello world!")

@our_decorator
def succ(n):
    return n + 1

@our_decorator
def add(x,y):
    return x+y

@our_decorator
def ss(list):
    return sum(list)


def main():
    print("printMsg() = %s" % printMsg())
    print("succ(1) = %s"%succ(1))
    print("add(1,2) = %s" % add(1,2))
    print("ss([1,2,3]) = %s" % ss([1,2,3]))
    print("succ(2) = %s" % succ(2))


if __name__ == "__main__":
    main()