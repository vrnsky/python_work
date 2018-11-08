class Restaurant():
	"""Simple model of the restaurant"""
	def __init__(self, restaurant_name, cuisine_type, numbed_served='0'):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.numbed_served = int(numbed_served)


	def describe_restaurant(self):
		print("Name of the restaurant: " + self.restaurant_name)
		print("Cuisine type of the restaurant: " + self.cuisine_type)


	def open_restaurant(self):
		print("The " + self.restaurant_name + " is open")

	def set_numbed_served(self, count):
		if self.numbed_served < count:
			self.numbed_served = count
		else:
			print('You shall not pass')

	def increment_numbed_served(self, increment):
		self.numbed_served += increment

class IceCreamStand(Restaurant):
	"""Docs"""

	def __init__(self, name, cuisine_type, numbed_served, flavors):
		super().__init__(name, cuisine_type, numbed_served)
		self.flavors = flavors

	def print_flavors(self):
		for flavor in self.flavors:
			print(flavor)