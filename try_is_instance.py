class MyMetaclass(type):
    pass


class BaseClass:
    pass


class DerivedClass(BaseClass, metaclass=MyMetaclass):
    pass

def main():
    b = BaseClass()
    d = DerivedClass()
    print(isinstance(b, DerivedClass))

if __name__ == '__main__':
    main()