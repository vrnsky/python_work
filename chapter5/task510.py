current_users = ["vrnsky", "voronyansky", "evrnsky", "avrnsky", "andr.vrnsky"]
new_users = current_users[:]
new_users.append("Arisha Voronyansky")
new_users.append("Helen Voronyansky")

for user in new_users:
	if user.lower() in current_users:
		print("You must need create a new name")
	else:
		print("You name is free")