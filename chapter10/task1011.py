import json

number = input("Enter your favourite number\n")

print("Start writing to the file\n")
with open("favourite.json", 'w') as file:
	json.dump(number, file)

file.close()
print("Finish writing to the file\n")

print("Start reading from file\n")
with open("favourite.json") as file:
	content = json.load(file)

print(content)

file.close()
print("Finish reading from file")