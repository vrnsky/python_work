import json

filename = "username.json"
def get_stored_user():
	try:
		with open(filename, 'r') as file:
			number = json.load(file)
	except FileNotFoundError:
		return None
	else:
		file.close()
		return number

def greetings_user():
	username = get_stored_user()
	if username:
		print("Welcome back " + username + " !")
	else:
		username = input("Enter your name\n")
		print(username + " you entered a first time, now you will be saved\n")
		with open(filename, 'w') as file:
			json.dump(username, file)

greetings_user()