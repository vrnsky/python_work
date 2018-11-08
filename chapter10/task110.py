try:
	with open("book.txt") as bookFile:
		bookContent = bookFile.read()
except FileNotFoundError:
	print("Required file is missed!")
else:
	print(bookContent.lower().count("oof"))