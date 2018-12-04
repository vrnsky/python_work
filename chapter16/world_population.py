﻿import json
import pygal
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code

filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)


cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = pop_dict['Country Code'][0:2]
		if code:	
			print(code + ': ' + str(population))
			cc_populations[code.lower()] = population
		else:
			print('Error - ' + country_name)

# before render it needs sort by population
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 999999999:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


wm_style = RotateStyle('#336699')
wm  = pygal.maps.world.World(style=wm_style, base_style=LightColorizedStyle)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_populations.svg')