from unittest.mock import MagicMock

class Person:

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def print_name(self):
        print(self._name)
        return 7

    def get_age(self):
        return 30

    def echo(self, st, num):
        return st

def main():
    p = Person()
    p.print_name = MagicMock(return_value=10)
    p.echo = MagicMock(return_value='aa')
    print(p.echo('qq', 12))
    print(p.echo('rr', 14))
    p.echo.assert_any_call('qq', 12)
    p.echo.reset_mock()
    p.echo.assert_not_called()


if __name__ == '__main__':
    main()