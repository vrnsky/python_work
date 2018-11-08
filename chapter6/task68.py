pets = {
	'barsik' : {
	    'name':'barsik',
		'type':'cat',
		'age':3,
		'owner':'yegor'
	},
	'ryzhik': {
		'name':'ryzhik',
		'type':'cat',
		'age':5,
		'owner':'yegor'
	},
	'liza' : {
		'name':'liza',
		'type':'cat',
		'age':6,
		'owner':'olga'
	}
}

for pet in pets.values():
	print(pet['name'].title() + " " + str(pet['age']) + " year old. Name of owner: " + pet['owner'])
