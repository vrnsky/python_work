class Employee:

	def __init__(self, firstname, surname, salary):
		self.firstname = firstname
		self.surname = surname
		self.salary = salary

	def give_raise(self, amount=5000):
		if amount:
			self.salary += amount
		else:
			self.salary += amount

	def get_salary(self):
		return self.salary