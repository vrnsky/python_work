rivers = {
	'nile':'egypt',
	'volga':'russia',
	'amazon':'brasilia'
}

for key, value in rivers.items():
	print("The " + key.title() + " runs through " + value.title())


for value in rivers.values():
	print(value)


for key in rivers.keys():
	print(key)  