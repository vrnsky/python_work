import unittest
from city import city_with_country

class CityTest(unittest.TestCase):

	def test_city_with_country(self):
		self.assertEquals(city_with_country('moscow', 'russia'), 'Moscow, Russia')

	def test_city_with_county_and_population(self):
		self.assertEquals(city_with_country('moscow', 'russia', '15 000 000'), 'Moscow, Russia - population 15 000 000')

unittest.main()