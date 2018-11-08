﻿class User():
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


class Admin(User):
	"""More privilige user"""
	def __init__(self, username, password):
		super().__init__('admin', 'admin', username, password)
		self.priviliges = Privileges(['allow_send_message', 'allow_delete_user', 'allow_ban_user', 'allow_edit'])

	def show_priveleges(self):
		self.priviliges.show()



class Privileges:
	"""It is a simple priviges"""
	def __init__(self, priviliges):
		self.priviliges = priviliges

	def show(self):
		for priv in self.priviliges:
			print(priv)

admin = Admin('admin', 'admin')
admin.show_priveleges()