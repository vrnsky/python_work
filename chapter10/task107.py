while True:
	try:
		one = input("Enter a first number\n")

		if one == "q":
			break

		two = input("Enter a second number\n")

		if two == "q":
			break
		
		sum = int(one) + int(two)
	except ValueError:
		print("You enter a not number value")
	else:
		print("Sum is " + str(sum))
		