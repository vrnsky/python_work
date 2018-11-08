sandwich_orders = ['big mac', 'pastarami', 'cheeseburger', 'pastarami', 'simple', 'programmers', 'pastarami']

print('===================== BEFORE ========================')
for sandwich in sandwich_orders:
	print(sandwich)

while 'pastarami' in sandwich_orders:
	sandwich_orders.remove('pastarami')

print('===================== AFTER ========================')
for sandwich in sandwich_orders:
	print(sandwich)
