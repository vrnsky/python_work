def sandwiches(*toppings):
	print('Your sandwich contains:')
	for top in toppings:
		print(top)


sandwiches('sausage', 'cheese')
sandwiches('mushrooms')
sandwiches('cheese', 'tomato', 'bicycle')