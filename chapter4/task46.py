numbers = [number for number in range(1,21, 2)]

for value in numbers:
	print(value)

print("The first three items in the list are:" + str(numbers[:3]))
print("Three items from the middle of the list are: " + str(numbers[4:7]))
print("The last items in the list are: " + str(numbers[-3:]))