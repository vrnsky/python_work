sandwich_orders = ['big mac', 'cheeseburger', 'simple', 'programmers']
finished_sandwiches = []

while sandwich_orders:
	current = sandwich_orders.pop()

	print('I made your ' + current + ' sandwich')
	finished_sandwiches.append(current)

for sandwich in finished_sandwiches:
	print('Cooked ' + sandwich)