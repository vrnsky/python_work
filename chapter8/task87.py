def make_album(author, album, songs='0'):
	music = {}
	music['author'] = author
	music['album'] = album
	if songs:
		music['songs'] = int(songs)
	return music


print(make_album('yegor', 'bit_style'))
print(make_album('tessa violet', 'crush'))
print(make_album('depeche mode', 'personal'))
print(make_album('depeche mode', 'personal', '10'))


message = ''

while message != 'quit':

	artist = input('Enter a name of the artist\n')
	if artist == 'quit':
		break

	album = input('Enter a name of the album\n')
	if album == 'quit':
		break

	songs = input('Enter a count of the songs\n')
	if album == 'quit':
		break

	message = input('If you wanna out of the program. Just type quit\n')
	if message == 'quit':
		break
	print(make_album(artist, album, songs))