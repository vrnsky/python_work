class User():
	"""Implementation of the user"""
	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password

	def describe_user(self):
		print(self.first_name + " " + self.last_name + " known as " + self.username + " on the our site and have password " + self.password)

	def greet_user(self):
		print("hello " + self.first_name)



yegor = User('yegor', 'voronyansky', 'vrnsky', 'asdasd')
yegor.describe_user()
yegor.greet_user()