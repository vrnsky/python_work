from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		print('Now will be proceed: code=' + code + ', name=' + name + ', country_name=' + country_name)
		if name == country_name:
			return code
		return None