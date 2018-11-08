import unittest
from employee import Employee

class Employee_Test(unittest.TestCase):

	def setUp(self):
		self.employee = Employee('Yegor', 'Voronyansky', 20)


	def test_default_raise(self):
		self.employee.give_raise()
		self.assertEquals(self.employee.get_salary(), 5020)

	def test_custom_raise(self):
		self.employee.give_raise(1000)
		self.assertEquals(self.employee.get_salary(), 1020)

unittest.main()