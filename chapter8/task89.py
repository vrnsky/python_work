def show_magicans(magicans):
	for magican in magicans:
		print('Everyone, hi! Me name is ' + magican)

def make_great(magicans):
	great_magic = []
	while magicans:
		current = magicans.pop()
		great_magic.append('Great ' + current)

	return great_magic

magicans = ['Yegor', 'Arisha', 'Ksusha', 'Peter']
great_magic = make_great(magicans)
show_magicans(great_magic)