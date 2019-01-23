#
#       Plotando histograma da soma de dois dados
#

import pygal

from die import Die

#   Cria dois dados D6
die_1 = Die()
die_2 = Die()
times = 1000

#   Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(times):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#   Analisa os resultados
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#   Visualiza os resultados
hist = pygal.Bar()

hist.tile = "Results of rolling two D6 dice " + str(times) + " times."
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.Y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('graphs/double_die_plot.svg')