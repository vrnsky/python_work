myFavouritePizza = ['pepperoni', 'ferrari', 'havai']
friendFavouritePizze = myFavouritePizza[:]

friendFavouritePizze.append('anotherPizza')

for pizza in myFavouritePizza:
	print(pizza)

print('==== FRIEND PIZZA ======')

for pizza in friendFavouritePizze:
	print(pizza)