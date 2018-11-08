cats = "cats.txt"
dogs = "dogs.txt"

try:
	with open("dogs.txt") as dogFile:
		dogNames = dogFile.read()
	with open("cats.txt") as catFile:
		catNames = catFile.read()
except FileNotFoundError:
	print("Required file does not found! Please check it!")
else:
	print(dogNames)
	print(catNames)