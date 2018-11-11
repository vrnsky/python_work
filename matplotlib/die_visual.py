from die import Die
import pygal

# Make some rolls, and store results in a list.
# Create a D6 and a D10.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
	result = die_1.roll() * die_2.roll() * die_3.roll()
	results.append(result)

# # Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# # Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a three D6 10,000 times."
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16', '17', '18']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_three_visual.svg')