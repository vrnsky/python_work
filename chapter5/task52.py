print('audi' == 'AUDI'.lower())
print('bmw' != 'audi')
print(1 != 0)
print(2 == 1)
print(1 > 0)
print(1 <= 0)
print(2 >= 3)

numbers = [number for number in range(1,11)]

if 1 in numbers:
	print("We have got a one hero!")

if not 11 in numbers:
	print("We have not got a hero!")