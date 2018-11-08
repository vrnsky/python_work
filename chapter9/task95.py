class User():
	"""Implementation of the user"""
	def __init__(self, first_name, last_name, username, password, login_attempts='0'):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.login_attempts = int(login_attempts)

	def describe_user(self):
		print(self.first_name + " " + self.last_name + " known as " + self.username + " on the our site and have password " + self.password)

	def greet_user(self):
		print("hello " + self.first_name)

	def increment_login_attemps(self):
		self.login_attempts += 1

	def reset_login_attemps(self):
		self.login_attempts = 0



yegor = User('yegor', 'voronyansky', 'vrnsky', 'asdasd')
yegor.describe_user()
yegor.greet_user()
yegor.increment_login_attemps()
yegor.increment_login_attemps()
yegor.increment_login_attemps()
yegor.increment_login_attemps()
yegor.increment_login_attemps()
yegor.increment_login_attemps()
yegor.increment_login_attemps()
yegor.increment_login_attemps()

print(yegor.login_attempts)
yegor.reset_login_attemps()
print(yegor.login_attempts)



