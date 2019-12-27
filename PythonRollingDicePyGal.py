import pygal
from random import randint


class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)

die = Die()

results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 Times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency o result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

die_1 = Die()
die_2 = Die()

resultstwo=[]
for roll_num in range(1000):
    resulttwo=die_1.roll() + die_2.roll()
    resultstwo.append(resulttwo)

frequenciestwo = []
max_result = die_1.num_sides + die_2.num_sides
for valuetwo in range(2, max_result+1):
    frequencytwo = resultstwo.count(valuetwo)
    frequenciestwo.append(frequencytwo)
print(frequenciestwo)

hist2 = pygal.Bar()

hist2.title = "Results of rolling two D6 1000 Times"
hist2.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist2.x_title = "Result"
hist2.y_title = "Frequency of result"

hist2.add('D6 + D6', frequenciestwo)
hist2.render_to_file('die_visual2.svg')