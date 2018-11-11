import matplotlib.pyplot as plt

input_values=list(range(1, 5000))
squares = [pow(x, 3) for x in input_values]
plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.scatter(input_values, squares, s=200, c=squares, cmap=plt.cm.Blues)
plt.show()