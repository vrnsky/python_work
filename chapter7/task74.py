prompt = 'Enter a name of the topping\n'
message = '';

while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print('Added to your pizzan this topping ' + message)