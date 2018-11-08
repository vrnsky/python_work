peoples = {
	'arisha' : {
		'firts_name':'Arisha',
		'last_name':'Voronyanskaya',
		'city':'Oktyabrsky'
		},
	'yegor' : {
		'firts_name':'Yegor',
		'last_name':'Voronyansky',
		'city':'Oktyabrsky'
	},
	'valentina' : {
		'firts_name':'valentina',
		'last_name':'popova',
		'city':'Moscow'	
	}
}


for value in peoples.values():
	print(value['firts_name'] + " " + value['last_name'] + " lives in " + value['city']);

