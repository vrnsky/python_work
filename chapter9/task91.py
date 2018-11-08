class Restaurant():
	"""Simple model of the restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		print("Name of the restaurant: " + self.restaurant_name)
		print("Cuisine type of the restaurant: " + self.cuisine_type)


	def open_restaurant(self):
		print("The " + self.restaurant_name + " is open")

restaurant = Restaurant('Yegorka Partty', 'Hmmmm I don not know')
restaurant.describe_restaurant()
restaurant.open_restaurant()
another_rest = Restaurant('Arisha Holiday', 'AdAsdsad')
another_rest.describe_restaurant()
yet_rest = Restaurant('MAsdas', 'asddsa')
another_rest.describe_restaurant()