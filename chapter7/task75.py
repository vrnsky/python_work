prompt = "Enter a your age\n"
message = ''
lowCost = 'free'
mediumCost = '10 $'
highCost = '15 $'

while message != 'quit':

	if message == 'quit':
		break
	message = input(prompt)
	age = int(message)
	if age <= 3:
		print('Your age ' + str(age) + '. Cost of ticket - ' + lowCost)
	elif age > 3 and age <= 12:
		print('Your age ' + str(age) + '. Cost of ticket - ' + mediumCost)
	elif age > 12:
		print('Your age ' + str(age) + '. Cost of ticket - ' + highCost)

