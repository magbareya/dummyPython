from unittest import TestCase

from my_mathh import MyMath


class MyTests(TestCase):
	def test_multiply(self):
		calc = MyMath()
		assert calc.mul(2,3) == 6
	
	def test_power(self):
		calc = MyMath()
		assert calc.power(2,2) == 4