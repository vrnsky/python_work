one = input("Enter a first number\n")
two = input("Enter a second number\n")

try:
	sum = int(one) + int(two)
except ValueError:
	print("You enter a not number value")
else:
	print("Sum is " + str(sum))