from collections import OrderedDict

favourite_languages = OrderedDict()
favourite_languages['yegor'] = 'Java'
favourite_languages['arisha'] = 'Python'


for name, language in favourite_languages.items():
	print(name.title() + " favourite language is " + language)