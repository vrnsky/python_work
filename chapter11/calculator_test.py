import unittest
from calculator import sum

class CalculatorTestCase(unittest.TestCase):

	def test_sum(self):
		self.assertEquals(20, sum(10, 10))


unittest.main()