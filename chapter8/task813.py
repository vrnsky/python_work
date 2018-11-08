def build_profile(username, password, **options):
	profile = {}
	profile['username'] = username
	profile['password'] = password

	for key, value in options.items():
		profile[key] = value

	return profile

print(build_profile('vrnsky', 'asdasda', location='Russian Federation', programmingOn='java', groups='dev'))
print(build_profile('varishka', 'asdasdasda', location='USA', programmingOn='kotlin', groups='dev'))
print(build_profile('vyegorka', 'asdasdasda', location='Canada', programmingOn='python', groups='testing'))